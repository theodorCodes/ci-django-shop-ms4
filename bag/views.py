from django.shortcuts import render, redirect, reverse, HttpResponse


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



# Adjust bag items
# It still takes the request and item id as parameters.
def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product to the shopping amount """

    # product = get_object_or_404(Product, pk=item_id)

    # And the entire top portion
    # will be the same except we don't need the redirect URL since we'll always want
    # to redirect back to the shopping bag page.
    quantity = int(request.POST.get('quantity'))
    # redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        # Remember that this is coming from a form on the shopping bag page which will
        # contain the new quantity the user wants in the bag. 
        # So the basic idea here is that if quantity is greater than zero 
        if quantity > 0:
            # we'll want to set the items quantity accordingly 
            bag[item_id]['items_by_size'][size] = quantity
            # response message
            # messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            # and otherwise we'll just remove the item.
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            # response message
            # messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')

    # Summary to aboves if statement:        
    # If there's a size. Of course we'll need to drill into the
    # items by size dictionary, find that specific size and either set its
    # quantity to the updated one or remove it if the quantity submitted is zero.

    # Summary to below else statement:
    # If there's no size that logic is quite simple and we can remove the item
    # entirely by using the pop function.
    else:
        if quantity > 0:
            bag[item_id] = quantity
            # response message
            # messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            # response message
            # messages.success(request, f'Removed {product.name} from your bag')
    # These two operations are basically the same.
    # They just need to be handled differently due to the more complex structure of the
    # bag for items that have sizes.

    request.session['bag'] = bag
    # With that finished we just need to redirect back
    # to the view bag URL. And I'll use the reverse function to do that.
    # Importing it here at the top, see TOP
    return redirect(reverse('view_bag'))


# Remove bag item
# change name to remove_from_bag
def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """

    try:
        # adding product here
        # product = get_object_or_404(Product, pk=item_id)

        # We don't need the quantity in this view since the intended quantity is zero.
        ## quantity = int(request.POST.get('quantity'))
        # Now if the user is removing a product with sizes.
        # We want to remove only the specific size they requested.
        # So if size is in request.post, such as in *a) and in *b)
        # We'll want to delete that size key in the items by size dictionary at *c).
        size = None
        if 'product_size' in request.POST:
            # v-- *a)
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        #  v-- *b)
        if size:
            #                                 v-- *c)
            del bag[item_id]['items_by_size'][size]
            # Also if that's the only size they had in the bag.
            # In other words, if the items by size dictionary is now empty which will evaluate to false.
            if not bag[item_id]['items_by_size']:
                # We might as well remove the entire item id so we don't end up with an empty items
                # by size dictionary hanging around.
                bag.pop(item_id)
                # We should also do this in the adjust bag view if the quantity is set to zero.
                # See *d)
            # response message
            # messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
        else:
            # If there is no size. Again removing the item is as simple as popping it out of the bag.
            bag.pop(item_id)  ## TYPO HERE! change from: [item_id] to: (item_id) 
            # response message
            # messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        # Finally instead of returning a redirect.
        ## return redirect reverse 'view_bag'
        # Because this view will be posted to from a JavaScript function.
        # We want to return an actual 200 HTTP response.
        # Implying that the item was successfully removed.
        return HttpResponse(status=200)
    except Exception as e:
        # response message
        # messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)