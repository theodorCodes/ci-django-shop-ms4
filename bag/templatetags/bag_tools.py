# Import template from Django
from django import template

# Custom template tag and filter

# Register filter to calculate subtotal in bag.html
register = template.Library()

# Using decorator to register function as template filter
@register.filter(name='calc_subtotal')
# Then create function which takes price and quantity as parameter
# and returns their product (price multiplied by quantity)
def calc_subtotal(price, quantity):
    return price * quantity