from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404  # product shortcut
from products.models import Product  # product from model


def bag_contents(request):
    """
      Handles bag items, registrated in settings.py
      for project wide availability
    """
    # Store bag items in a list
    # Stores sum of all product prices
    # Stores number of items
    # Adding current bag items from session here, see bag/views.py
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    # Extract data for each item in bag variable
    for item_id, item_data in bag.items():
        # In the case of an item with no sizes, the item data will just be
        # the quantity (item_data, int)
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            # # Calculate total + quantity * price
            total += item_data * product.price
            # Increment product_count variable by quantity
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'category': product.category,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            # But in the case of an item that has sizes, the item data will be
            # a dictionary of all the items by size ['items_by_size']
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                # Then store variables in bag_items including product
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,  # Holds the actual size (!)
                    'category': product.category,
                })

    # Converting object to string inside list comprehension
    # and save available categories in categories_found variable
    categories_found = [str(category['category']) for category in bag_items]
    # Percentage based 'delivery' cost calculation
    # If category artwork found and total is smaller then (50)
    if 'artwork' in categories_found and \
            total < settings.FREE_DELIVERY_THRESHOLD:
        # Estimate delivery (total * 10 / 100)
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        # Estimate missing sum to reach (50) for free delivery
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    # Else if artwork is above (50) then delivery is free
    else:
        delivery = 0
        free_delivery_delta = 0
    grand_total = delivery + total
    # This context from all other templates as its registered in settings.py
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }
    return context
