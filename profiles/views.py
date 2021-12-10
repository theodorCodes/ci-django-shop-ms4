from django.shortcuts import render

def profile(request):
    """ Display user profile """
    # Store template
    template = 'profiles/profile.html'
    context = {
        
    }
    return render(request, template, context)
