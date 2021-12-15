from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404  # product shortcut
from products.models import Product  # product from model


def bag_contents(request):
    """ Handles bag items, registrated in settings.py 
    for project wide availability """

    # 1) Variable bag_items stores bag items
    # 2) Variable total stores sum of all product prices
    # 3) Variable product_count stores number of items
    # 5) (session) Adding session 'bag' from bag/views.py here

    bag_items = []  # 1)
    total = 0  # 2)
    product_count = 0  # 3)
    bag = request.session.get('bag', {})  # 5)

    # In the case of an item with no sizes. 
    # The item data will just be the quantity.
    # But in the case of an item that has sizes 
    # the item data will be a dictionary of all the items by size.
    #
    # 6) (session) Extract data for each item in bag variable
    # Get product
    # Calc total + quantity * price
    # Increment product_count variable by quantity
    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'category': product.category,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                # Then store variables in bag_items including the product itself
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

    # 4) Percentage based 'delivery' cost calculation
    # a) Calculate shipping when item is physical item such as a 'print'
    #    AND when total is under 50 (see settings in settings.py)
    #    (for digital items delivery cost should be 0)
    # b) Estimate 'delivery' (total * 10 / 100)
    # c) Estimate missing sum to reach free delivery
    # d) Delivery is free when total is greater than 50
    # e) Grand total or final sum to be charged
    # f1) Making the following data avaible or accessible from other templates
    #    as this file is registered in project_main/settings.py
    # f2) return values saved in context

    # a)
    if 'print' in categories_found and total < settings.FREE_DELIVERY_THRESHOLD:
        # b)
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        # c)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        # d)
        delivery = 0
        free_delivery_delta = 0

    # e)
    grand_total = delivery + total

    # f1)
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    # f2)
    return context