from django.shortcuts import render


# Bag view function view_bag()
def view_bag(request):
    """ Show bag page """

    return render(request, 'bag/bag.html')