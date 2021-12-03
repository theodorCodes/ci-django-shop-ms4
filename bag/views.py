from django.shortcuts import render, redirect


# Renders bag view
def view_bag(request):
    """ Show bag page """

    return render(request, 'bag/bag.html')


# Creates add to bag session, submitting with item_id info
def add_to_bag(request, item_id):
    """ Add product and quantity to the shopping bag """

    # Once submitted:
    # Get and store quantity
    # Get and store redirect_url
    # Get and store existing bag variable, or create 'bag' session variable
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        # Update the quantity
        bag[item_id] += quantity
    else:
        # Add item to 'bag'
        bag[item_id] = quantity

    # Then overwrite session with updated bag info
    request.session['bag'] = bag

    # TEST output of content stored in 'bag' session
    # print(request.session['bag'])
    # Outputs: {'2': 1}
    # Which translates to item_id '2' with quantity of 1

    # Redirect user back to redirect_url
    return redirect(redirect_url)