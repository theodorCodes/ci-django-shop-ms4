from django.shortcuts import render, redirect


# Bag view function
def view_bag(request):
    """ Show bag page """

    return render(request, 'bag/bag.html')


# Add to bag function, submits with item_id info
def add_to_bag(request, item_id):
    """ Add product and quantity to the shopping bag """

    # Once submitted:
    # Get and store quantity
    quantity = int(request.POST.get('quantity'))
    # Get and store redirect_url
    redirect_url = request.POST.get('redirect_url')
    # Get and store bag variable, or create
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        # Update the quantity
        bag[item_id] += quantity
    else:
        # Add item to the bag
        bag[item_id] = quantity

    # Then overwrite session with updated bag info
    request.session['bag'] = bag

    # Print to check content stored session
    print(request.session['bag'])
    # Outputs: {'2': 1}
    # Which translates to item '2' with quantity of 1

    # Redirect user back to redirect_url
    return redirect(redirect_url)