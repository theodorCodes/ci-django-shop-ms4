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


    # 6) (session) Extract data for each item in bag variable
    # Get product
    # Calc total + quantity * price
    # Increment product_count variable by the quantity
    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity

        # Then store variables in bag_items including the product itself
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    # 4) Percentage based 'delivery' cost calculation
    # a) Calculate shipping when total is under 50 (see settings in settings.py)
    # b) Estimate 'delivery' (total * 10 / 100)
    # c) Estimate missing sum to reach free delivery
    # d) Delivery is free when total is greater than 50
    # e) Grand total or final sum to be charged
    # f) Making the following data avaible or accessible from other templates
    #    as this file is registered in project_main/settings.py
    # g) return values

    if total < settings.FREE_DELIVERY_THRESHOLD:
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

    # f)
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    # g)
    return context