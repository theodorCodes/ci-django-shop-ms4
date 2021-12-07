from django.shortcuts import render, redirect, reverse  # redirect and reverse
from django.contrib import messages  # Import messages
from .forms import OrderForm  # Import order form


# Checkout view
def checkout(request):
    # Get bag saved in session
    bag = request.session.get('bag', {})
    if not bag:
        # Response message when bag is empty
        messages.error(request, "There's nothing in your bag at the moment")
        # Redirect to products template, prevents manual url access to /checkout
        return redirect(reverse('products'))
    
    # Create empty instance of order form
    order_form = OrderForm()
    # Create template
    template = 'checkout/checkout.html'
    # Create context
    context = {
        'order_form': order_form,
        # Test Stripe public key
        'stripe_public_key': 'pk_test_51JuyiqFRX12E4U8SGMFixDSoY5AtCCjYIgP0YQANwjzbMrXSkiO0MVYQDcRfao4PM5VrlZkmINlLOgPxLcxqglO700kmdwOlBZ',
        # Test Stripe secret key
        'client_secret': 'test client secret',
    }

    # Render
    return render(request, template, context)