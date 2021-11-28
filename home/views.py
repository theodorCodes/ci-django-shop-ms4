from django.shortcuts import render

# Home view
def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index.html')