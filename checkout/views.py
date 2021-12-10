# Added redirect, reverse and get product, and HttpResponse for card payment
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST  # Import for card payment
from django.contrib import messages  # Import messages
from django.conf import settings  # Import settings to use with Stripe

from .forms import OrderForm  # Import order form
from .models import Order, OrderLineItem  # Import Order, OrderLineItem from this app
from products.models import Product  # Import Product from product model
from bag.contexts import bag_contents  # Import context from bag
import stripe  # Import Stripe after installation
import json  # Import json to save bag metadata during card payment


# Using post decorator to allow post request from stripe_elements.js only
# Requires routing in urls.py
@require_POST
def cache_checkout_data(request):
    # Try this to get 200 response. In this view:
    try:
        # Save client secret in pid, process id
        pid = request.POST.get('client_secret').split('_secret')[0]
        # Save Stripe key
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # Modify content by adding metadata such as
        stripe.PaymentIntent.modify(pid, metadata={
            # Bag info using json
            'bag': json.dumps(request.session.get('bag', {})),
            # Save user boolean info
            'save_info': request.POST.get('save_info'),
            # Username
            'username': request.user,
        })
        # Once info gathered respond with 200
        return HttpResponse(status=200)
    except Exception as e:
        # Otherwise repsond with error message and return a 400 response
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


# Checkout view - payment process
def checkout(request):
    # Get Stripe keys referenced in settings
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Stripe checkout flow with POST, user data
    # Check if method is POST
    if request.method == 'POST':
        # Get shopping bag items
        bag = request.session.get('bag', {})
        # Manually put data from form into form_data dictionary, to skip infobox
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        # Then create instance with the form_data
        order_form = OrderForm(form_data)
        # If order is valid, save order form
        if order_form.is_valid():
            # Prevent multiple save events on database
            order = order_form.save(commit=False)
            # Get payment intent id from secret
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            # Dump bag into json string
            order.original_bag = json.dumps(bag)
            # Save order
            order.save()
            # Iterating through bag to create each line item
            for item_id, item_data in bag.items():
                try:
                    # Get product id
                    product = Product.objects.get(id=item_id)
                    # If item id is integer it has no format or size,
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            # and quantity will be the item_data
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        # Otherwise if item has size, iterate through sizes
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                # and quantity will be the quantity
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                # If no product
                except Product.DoesNotExist:
                    # Respond with message
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    # And delete empty order
                    order.delete()
                    # And return user bag to shopping bag page
                    return redirect(reverse('view_bag'))
            # Save user intent to save_info in session for checkout_success
            request.session['save_info'] = 'save-info' in request.POST
            # And return to checkout_success page including order number
            return redirect(reverse('checkout_success', args=[order.order_number]))
        # If order is not valid
        else:
            # Response message
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    # In case method is not POST
    else:
        ## Stripe payment intent without POST data
        # Get bag saved in session
        bag = request.session.get('bag', {})
        if not bag:
            # Response message when bag is empty
            messages.error(request, "There's nothing in your bag at the moment")
            # Redirect to products template, prevents manual url access to /checkout
            return redirect(reverse('products'))

        # Stripe
        # Store request from bag in current_bag
        current_bag = bag_contents(request)
        # And get grand_total from current_bag
        total = current_bag['grand_total']
        # Then multiply total by 100 and round it to zero decimal to produce integer
        stripe_total = round(total * 100)
        # Set secret key on Stripe
        stripe.api_key = stripe_secret_key
        # Then create payment intent
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # TEST: intent by printing 'intent' to console
        # RESULT: print Stripe response to console successful

        # Create empty instance of order form
        order_form = OrderForm()

    # Set response message in case Stripe key is not working
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    # Create template
    template = 'checkout/checkout.html'
    # Create context
    context = {
        'order_form': order_form,
        # Stripe public key
        'stripe_public_key': stripe_public_key,
        # Stripe intent client secret
        'client_secret': intent.client_secret,
    }
    # Render
    return render(request, template, context)



# Checkout success view
def checkout_success(request, order_number):
    # Save user intent to save_info from session saved above
    save_info = request.session.get('save_info')
    # Get order number
    order = get_object_or_404(Order, order_number=order_number)

    # Response message that order was successful and email will be send
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')
    # Delete shopping bag from session as no longer required
    if 'bag' in request.session:
        del request.session['bag']
    # Set template and context
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    # Render template
    return render(request, template, context)