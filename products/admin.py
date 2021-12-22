from django.contrib import admin
# Import category, type, format and product model
from .models import Product, Category, Format, Type


class ProductAdmin(admin.ModelAdmin):
    """ Create 'ProductAdmin' class """
    # to display all 'list_display' items as described below
    # in the same row under 'Products' in admin
    # By default Django list only the first item
    list_display = (
        'name',
        'category',
        'created_by',
        'sku',
        'type',
        'format',
        'description',
        'has_sizes',
        'price',
        'rating',
        'image',
    )


class CategoryAdmin(admin.ModelAdmin):
    """ Create 'CategoryAdmin' class """
    # to display both in one row,
    # 'friendly name' and 'name' from model in admin under 'Categories'
    # By default Django lists only the 'name'
    list_display = (
        'friendly_name',
        'name',
    )


class TypeAdmin(admin.ModelAdmin):
    """ Create 'TypeAdmin' class """
    # to display both in one row,
    # 'friendly name' and 'name' from model in admin under 'Categories'
    # By default Django lists only the 'name'
    list_display = (
        'friendly_name',
        'name',
    )


class FormatAdmin(admin.ModelAdmin):
    """ Create 'FormatAdmin' class """
    # to display both in one row,
    # 'friendly name' and 'name' from model in admin under 'Categories'
    # By default Django lists only the 'name'
    list_display = (
        'friendly_name',
        'name',
    )


# Register 'Category', 'Type', 'Format' and 'Product' model for admin page
# and the 2 created classes created above
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Format, FormatAdmin)
