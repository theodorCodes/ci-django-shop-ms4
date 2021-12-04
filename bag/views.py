from django.shortcuts import render, redirect


# Renders bag view
def view_bag(request):
    """ Show bag page """

    return render(request, 'bag/bag.html')


# Creates add to bag session, submitting with item_id info
def add_to_bag(request, item_id):
    """ Add product and quantity to the shopping bag """

    # B1 Once submitted, from form:
    # Get and store quantity
    # Get and store redirect_url
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    # S1 Create size variable with None value
    size = None
    # S2 then get product_size if available from product_detail.html
    # and store it in size variable
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # B2 Get bag items from session created in contexts.py, or create
    bag = request.session.get('bag', {})

    # S3
    # If size or format is available and
    # if item is in the bag and
    # if another another item with the same id is in the bag
    # increment quantity
    # else set current quantity to bag that has size
    # with success message
    # else add to bag as dictionary with the key of items_by_size.
    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                # messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                # messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            # messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
    # B3
    # if no size then just add quantity
    else:
        # B3
        if item_id in list(bag.keys()):
            # Update the quantity
            bag[item_id] += quantity
            # messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            # Add item to 'bag'
            bag[item_id] = quantity
            # messages.success(request, f'Added {product.name} to your bag')

    # B4 Then overwrite session with updated bag info
    request.session['bag'] = bag

    # TEST output of content stored in 'bag' session
    # print(request.session['bag'])
    # Outputs: {'2': 1}
    # Which translates to item_id '2' with quantity of 1

    # B5 Redirect user back to redirect_url
    return redirect(redirect_url)