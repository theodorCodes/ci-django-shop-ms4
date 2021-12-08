from django.contrib import admin
# Import OrderLineItem model
from .models import Order, OrderLineItem


# Allows to add and edit items on the same page
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    # Specify readonly fields
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',)

    # Editable fields
    fields = (
        'order_number',
        # 'user_profile',
        'date',
        'full_name',
        'email',
        'phone_number',
        'country',
        'postcode',
        'town_or_city',
        'street_address1',
        'street_address2',
        'county',
        'delivery_cost',
        'order_total',
        'grand_total',
    )

    # Specify or limit visible fields under Checkout > Orders
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    # Set orders to be ordered chronologically by date - newest on top
    ordering = ('-date',)

# Register Order and OrderAdmin in Django admin
admin.site.register(Order, OrderAdmin)