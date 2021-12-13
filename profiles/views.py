from django.shortcuts import render, get_object_or_404  # Import products
from django.contrib import messages  # Import messages
from django.contrib.auth.decorators import login_required  # Login decorator
from .models import UserProfile  # Import profiles from models
from .forms import UserProfileForm  # Import the form function from forms.py
from checkout.models import Order  # Import checkout order to get order_number

# Using login decorator
@login_required
def profile(request):
    """ Display user profile """
    # Return profile to template
    profile = get_object_or_404(UserProfile, user=request.user)

    # If request is post
    if request.method == 'POST':
        # Use post data to create user profile instance with imported form
        form = UserProfileForm(request.POST, instance=profile)
        # If form valid
        if form.is_valid():
            # Save and publish response message
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        # Populate form variable with user's current profile information
        form = UserProfileForm(instance=profile)
    # Return the profile with the order, 
    # instead of adding user profile to context
    orders = profile.orders.all()

    # Store template
    template = 'profiles/profile.html'

    # Add profile to context, without profile as it is returned within orders
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    # Render this in profile.html template
    return render(request, template, context)


# for order history in profile.html
def order_history(request, order_number):
    # Get order
    order = get_object_or_404(Order, order_number=order_number)

    # Response message
    messages.info(request, (
        f'This is a post confirmation for order number { order_number }.'
        'A confirmation email was sent on the order date.'
    ))


    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)