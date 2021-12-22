from django.db import models
from profiles.models import UserProfile  # Import from profiles/models.py


class Category(models.Model):
    """ In stock product category table """
    # Fixes plural spelling for the word 'Categories' title in admin page
    class Meta:
        verbose_name_plural = 'Categories'

    # Creating 2 fields in the 'Category' table
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)


    def __str__(self):
        """ String method to return human readable string representation """
        return self.name


    def get_friendly_name(self):
        return self.friendly_name


class Type(models.Model):
    """ Configurable product type selection table """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)


    def __str__(self):
        return self.name


    def get_friendly_name(self):
        return self.friendly_name


class Format(models.Model):
    """ Configurable format selection table """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)


    def __str__(self):
        return self.name


    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """ In stock and configurable product table """
    # Creating relationship to 'Category' table
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    # Creating relationship to 'Type' table
    type = models.ForeignKey(
        'Type', null=True, blank=True, on_delete=models.SET_NULL)
    # Creating relationship to 'Format' table
    format = models.ForeignKey(
        'Format', null=True, blank=True, on_delete=models.SET_NULL)
    # Other fields in 'Product' table
    sku = models.CharField(max_length=12, null=True, blank=True)
    name = models.CharField(max_length=254)
    created_by = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.IntegerField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.name
