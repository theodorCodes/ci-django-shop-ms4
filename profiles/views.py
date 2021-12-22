from django.shortcuts import render, get_object_or_404  # Import products
from django.contrib import messages  # Import messages
from django.contrib.auth.decorators import login_required  # Login decorator
from .models import UserProfile  # Import profiles from models
from .forms import UserProfileForm  # Import the form function from forms.py
from checkout.models import Order  # Import checkout order to get order_number
from products.models import Product, Category, Type, Format  # Import products


# Using login decorator
@login_required
def profile(request):
    """ Display user shipping info """
    # Get profile name of authenticated user
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
            messages.error(request, 'Update failed.\
              Please ensure the form is valid.')
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


@login_required
def profile_custom_products(request):
    """ Display user purchases """
    # Get profile name of user
    profile = get_object_or_404(UserProfile, user=request.user)
    # Get products created by user
    products = Product.objects.filter(created_by=request.user)
    # Use this template
    template = 'profiles/profile_custom_products.html'
    # Template context
    context = {
        'profile': profile,
        'products': products,
    }
    # Render this in profile.html template
    return render(request, template, context)


@login_required
def profile_custom_orders(request):
    """ Display users purchases """
    # Get profile name of authenticated user
    profile = get_object_or_404(UserProfile, user=request.user)
    # If request is post
    if request.method == 'POST':
        # Get user form with info
        form = UserProfileForm(request.POST, instance=profile)
        # If form valid
        if form.is_valid():
            # Save and publish response message
            form.save()
    else:
        # Populate form variable with user's current profile information
        form = UserProfileForm(instance=profile)
    # Return the profile with the order,
    # instead of adding user profile to context
    orders = profile.orders.all()
    # Store template
    template = 'profiles/profile_custom_orders.html'
    # Add profile to context, without profile as it is returned within orders
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }
    # Render this in profile.html template
    return render(request, template, context)


def order_history(request, order_number):
    """ Order history for each profile """
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


@login_required
def order_overview(request):
    """ Display all orders for superuser """
    # Get orders
    orders = Order.objects.all()
    # Use this template
    template = 'profiles/allorders.html'
    # Template context
    context = {
        'orders': orders,
    }
    return render(request, template, context)
