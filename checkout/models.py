# Create checkout_order table and
# Create checkout_orderlineitem table in db

import uuid  # Generates order numbers
from django.db import models
from django.db.models import Sum  # Imports sum function from Django models
from django.conf import settings  # Imports settings module from django.conf

# installation of django-countries library required
from django_countries.fields import CountryField

from products.models import Product  # Import products


# Data to handle all orders
class Order(models.Model):
    # Non editable order number
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    # Auto date field
    date = models.DateTimeField(auto_now_add=True)
    # Content to be calculated in methods below
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    # Prevent order double entry by saving original shopping bag info
    original_bag = models.TextField(null=False, blank=False, default='')
    # Prevent order double entry by saving Stripe payment intent id
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')


    # Methods to calculate order content above
    # Generate random 32 character long order number using uuid
    def _generate_order_number(self):
        """
        Generate a random and unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    # Update total
    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        # Calculate sum of all items using aggregate function, or set to zero
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        # Calculate delivery cost based on values set in settings
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    # Override order number if it does not exist
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    # Return order number
    def __str__(self):
        return self.order_number


# Order line items to specify each item in the order
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=20, null=True, blank=True)  # format A3 PRINT
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)


    # Calculate subtotal for each product in the order
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    # Return sku for each product in the order
    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'