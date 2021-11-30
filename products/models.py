from django.db import models


# Category table
class Category(models.Model):

    # Fixes plural spelling for the word 'Categories' title in admin page
    class Meta:
        verbose_name_plural = 'Categories'

    # Creating 2 fields in the 'Category' table
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    # String method to return human readable string representation
    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# Product table
class Product(models.Model):
    # Creating relationship to 'Category' table
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    # Other fields in 'Product' table
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    views = models.IntegerField(null=True, blank=True)
    likes = models.IntegerField(null=True, blank=True)
    comment = models.IntegerField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
