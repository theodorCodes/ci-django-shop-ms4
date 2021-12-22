import uuid  # Generates order numbers
from django.db import models
from django.db.models import Sum  # Imports sum function from Django models
from django.conf import settings  # Imports settings module from django.conf
from django_countries.fields import CountryField  # Requires django-countries
from products.models import Product  # Import products
from profiles.models import UserProfile  # Import from profiles/models.py


class Order(models.Model):
    """ Data to handle all orders, creates checkout_order table in db """
    # Non editable order number use with uuid
    order_number = models.CharField(max_length=32, null=False, editable=False)
    # ForeignKey to UserProfile and using models.SET_NULL to keep order record
    # when users deletes profile, allows purchases by visitors without profile
    # Making orders by profiles accessible via user.profile.order with 'orders'
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
            null=True, blank=True, related_name='orders')
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
    # Content to be calculated with methods below
    delivery_cost = models.DecimalField(max_digits=6,
            decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10,
            decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10,
            decimal_places=2, null=False, default=0)
    # Prevent order double entry by saving original shopping bag info
    original_bag = models.TextField(null=False, blank=False, default='')
    # Prevent order double entry by saving Stripe payment intent id
    stripe_pid = models.CharField(max_length=254,
            null=False, blank=False, default='')


    def _generate_order_number(self):
        """
        Generate random 32 character long and unique order number using UUID
        """
        return uuid.uuid4().hex.upper()


    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        # Calculate sum of all items using aggregate function, or set to zero
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))\
                ['lineitem_total__sum'] or 0
        # Calculate delivery cost based on values set in settings
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = \
                self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()


    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)


    def __str__(self):
        """ Return order number """
        return self.order_number


class OrderLineItem(models.Model):
    """
    Order line items to specify each item in the order
    Creates checkout_orderlineitem table in db
    """
    order = models.ForeignKey(Order, null=False,
            blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False,
            blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=20, null=True,
            blank=True)  # format A3 PRINT
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
            null=False, blank=False, editable=False)


    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total and update
        the order total by calculating subtotal for each product in the order
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)


    def __str__(self):
        """
        Return sku for each product in the order
        """
        return f'SKU {self.product.sku} on order {self.order.order_number}'
