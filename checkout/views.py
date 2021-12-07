from django.shortcuts import render, redirect, reverse  # redirect and reverse
from django.contrib import messages  # Import messages
from django.conf import settings  # Import settings to use with Stripe
from .forms import OrderForm  # Import order form
from bag.contexts import bag_contents  # Import context from bag
import stripe  # Import Stripe after installation



# Checkout view
def checkout(request):
    # Get Stripe keys referenced in settings
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

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

    # TEST intent
    # print(intent)  # print Stripe response to console successful

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



# 