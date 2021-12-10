from django.conf import settings  # Import settings to get Stripe credentials
from django.http import HttpResponse  # Import to check http responses
from django.views.decorators.http import require_POST  # Require Post requests
from django.views.decorators.csrf import csrf_exempt  # Exempts when no csrf
from checkout.webhook_handler import StripeWH_Handler  # Get webhook class
import stripe  # Imports Stripe

@require_POST  # Using imported decorator above to require POST requests
@csrf_exempt  # Using imported decorator above to make exemptions when no csrf

def webhook(request):
    """Listen for webhooks from Stripe"""
    # Setup credentials from settings.py
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
        payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    # Catch any other exeptions other than Stripe provided exceptions
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # TEST webhook view is working
    # print('Success!')
    # return HttpResponse(status=200)

    # Set up a webhook handler
    # Create instance and passing request
    handler = StripeWH_Handler(request)

    # Map webhook events to relevant handler functions
    # Create dictionary with keys from Stripe and methods
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }

    # Get the webhook type from Stripe
    event_type = event['type']

    # If there's a handler for it, get it from the event map
    # Use the generic one by default
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the event
    response = event_handler(event)
    return response
