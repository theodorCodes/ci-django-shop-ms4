from django.http import HttpResponse  # django.http
from .models import Order, OrderLineItem
from products.models import Product

import json
import time


# Webhook handler class
class StripeWH_Handler:
    """ Handle Stripe webhooks """
    # Access attributes from Stripe requests
    def __init__(self, request):
        self.request = request

    """ Handle a generic/unknown/unexpected webhook event """
    def handle_event(self, event):
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        # Handle payment intent succeeded webhook from Stripe
        # Will be sent each time a user completes a payment process

        # Save ent.data.object payment intent key in intent
        intent = event.data.object
        # TEST print intent
        # print(intent)

        # Save payment intent id, shopping bag, users save-info preference,
        # billing, shipping and grand total info
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean empty strings in shipping details and replace with None
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Create fail save order making assumptions
        # Assumption 1 - Order info does not exist
        order_exists = False
        attempt = 1
        # Looping 5 times
        while attempt <= 5:
            # Before creating actual order try to
            try:
                # get order from payment intent
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                # If order is found we set order_exists to True
                order_exists = True
                # break out of the loop once found
                break
            # If the order cannot be found
            except Order.DoesNotExist:
                # increment attempt + 1
                attempt += 1
                # and use Pythons time module to snooze for one second
                # This will in effect cause the webhook handler 
                # to try to find the order five times over five seconds
                # before giving up and creating the order itself.
                time.sleep(1)
        # Outside of the loop, check weather order exists
        if order_exists:
            # Order confirmation email
            self._send_confirmation_email(order)
            # And return 200 response
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        # If if does not exist, set order to none and create order without form
        else:
            order = None
            try:
                # Creating order without form using data from payment intent
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                # Creating bag items by iterating through payment intent json
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            # If the creation fails delete the order
            except Exception as e:
                if order:
                    order.delete()
                # 500 response will Stripe to automatically try webhook again
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        # Finally after above steps return 200 response
        # Order confirmation email
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)


    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        # Listening for payment failing
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
