from decimal import Decimal
from django.conf import settings


def bag_contents(request):
    """ Handles bag items, registrated in settings.py 
    for project wide availability """

    # Variable bag_items stores bag items
    bag_items = []

    # Variable total stores sum of all product prices
    total = 0

    # Variable product_count stores number of items
    product_count = 0

    # Calculating when free shipping is applicable
    # Percentage based 'delivery' cost calculation
    # Assumption and current setting:
    # FREE_DELIVERY_THRESHOLD = 50
    # STANDARD_DELIVERY_PERCENTAGE = 10 
    # Calculate shipping when total is under 50
    if total < settings.FREE_DELIVERY_THRESHOLD:
        # Estimate shipping cost
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        # Estimate missing sum to reach free delivery
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    # When total is greater then 50
    else:
        # Delivery is free
        delivery = 0
        free_delivery_delta = 0
    # Grand total or final sum to be charged
    grand_total = delivery + total

    # This file is registered in project_main/settings.py
    # making the following data avaible or accessible from other templates
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