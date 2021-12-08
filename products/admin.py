from django.contrib import admin
# Import category and product model
from .models import Product, Category


# Register your models here.
# Create 'ProductAdmin' class
class ProductAdmin(admin.ModelAdmin):
    # to display all 'list_display' items as described below
    # in the same row under 'Products' in admin
    # By default Django list only the first item
    list_display = (
        'name',
        'sku',
        'category',
        'description',
        'has_sizes',
        'price',
        'views',
        'likes',
        'comment',
        'image',
    )


# Create 'CategoryAdmin' class
class CategoryAdmin(admin.ModelAdmin):
    # to display both in one row,
    # 'friendly name' and 'name' from model in admin under 'Categories'
    # By default Django lists only the 'name'
    list_display = (
        'friendly_name',
        'name',
    )


# Register 'Category' and 'Product' model for admin page
# and the 2 created classes created above
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)