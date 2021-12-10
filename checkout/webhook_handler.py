from django.http import HttpResponse  # django.http


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
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        # Listening for payment failing
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)