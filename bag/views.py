from django.shortcuts import render, redirect, reverse, \
    HttpResponse, get_object_or_404
from django.contrib import messages  # Import for messages
from products.models import Product  # Import products


def view_bag(request):
    """ Render bag template """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
      Updates bag items in session,
      by adding product and quantity to the shopping bag
    """
    # Get product where primary key is item_id
    product = Product.objects.get(pk=item_id)
    # Save quantity as integer values
    quantity = int(request.POST.get('quantity'))
    # Get redirect url
    redirect_url = request.POST.get('redirect_url')
    # Create size variable and set to None value
    size = None
    # If product_size available from product_detail.html store it in size
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # Get bag items from session, see contexts.py, or create {} empty dict
    bag = request.session.get('bag', {})

    # If size or (print format) available and
    # if item is in the bag and
    # if another another item with the same id is in the bag
    # increment quantity
    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated format {size.upper()} \
                    {product.name} quantity to \
                    {bag[item_id]["items_by_size"][size]}')
            # Else set current quantity to bag that has size
            # with success message
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added format {size.upper()} \
                    {product.name} to your bag')
        # Else add to bag as dictionary with the key of items_by_size.
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added format {size.upper()} \
                {product.name} to your bag')
    # If no size then just add quantity
    else:
        if item_id in list(bag.keys()):
            # Update the quantity
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to \
                {bag[item_id]}')
        else:
            # Add item to 'bag'
            bag[item_id] = quantity
            # Test this message
            messages.success(request, f'Added {product.name} to your bag')

    # Then overwrite session with updated bag info
    request.session['bag'] = bag

    # TEST output of content stored in 'bag' session
    # print(request.session['bag'])
    # Outputs: {'2': 1}
    # Which translates to item_id '2' with quantity of 1

    # And redirect user back to redirect_url
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product to the shopping amount """
    # Get product by item id
    product = get_object_or_404(Product, pk=item_id)
    # Save quantity from shopping bag form as string value
    quantity = int(request.POST.get('quantity'))
    # Set size to None
    size = None
    # If product has size save it in size variable
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # Get bag items or save empty dict {} in bag variable
    bag = request.session.get('bag', {})

    # If there's a size and if quantity greater zero,
    # drill into the items by size dictionary, and find that specific size
    # and either set its quantity to the updated one
    # or remove it if the quantity submitted is zero.
    if size:
        if quantity > 0:
            # Set size for bag items with size equals quantity
            bag[item_id]['items_by_size'][size] = quantity
            # Response message
            messages.success(request, f'Updated format {size.upper()} \
                {product.name} quantity to \
                {bag[item_id]["items_by_size"][size]}')
        else:
            # If item has no size, remove the item.
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            # Response message
            messages.success(request, f'Removed format {size.upper()} \
                {product.name} from your bag')
    # If there's no size, remove the item entirely by using the pop function.
    else:
        if quantity > 0:
            bag[item_id] = quantity
            # Response message
            messages.success(request, f'Updated {product.name} quantity to \
                {bag[item_id]}')
        else:
            bag.pop(item_id)
            # Response message
            messages.success(request, f'Removed {product.name} from your bag')

    # Then overwrite session with updated bag info
    request.session['bag'] = bag

    # Redirect back to the view bag URL.
    # Using the Django reverse function to do that.
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """
    try:
        # Get product by item id
        product = get_object_or_404(Product, pk=item_id)
        # Set size to None
        size = None
        # If size available save it to size variable
        if 'product_size' in request.POST:
            size = request.POST['product_size']

        # Get bag items or save empty dict {} in bag variable
        bag = request.session.get('bag', {})

        # If size available
        if size:
            # Delete the size info first
            del bag[item_id]['items_by_size'][size]
            # Then if bag item has no item by size
            if not bag[item_id]['items_by_size']:
                # Delete item from list using pop()
                bag.pop(item_id)
                # We should also do this in the adjust bag view
                # if the quantity is set to zero.
                # See *d)
            # Response message
            messages.success(request, f'Removed format {size.upper()} \
                {product.name} from your bag')
        else:
            # If bag item has no item by size, delete using pop()
            bag.pop(item_id)
            # Response message
            messages.success(request, f'Removed {product.name} from your bag')

        # Then overwrite session with updated bag info
        request.session['bag'] = bag

        # And return positive Http response
        return HttpResponse(status=200)
    except Exception as e:
        # If something during this process does go wrong
        # Response message
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
