from django.shortcuts import render, get_object_or_404  # Import products
from .models import UserProfile  # Import profiles from models


def profile(request):
    """ Display user profile """
    # Return profile to template
    profile = get_object_or_404(UserProfile, user=request.user)
    # Store template
    template = 'profiles/profile.html'
    # Add profile to context
    context = {
        'profile': profile,
    }
    return render(request, template, context)
