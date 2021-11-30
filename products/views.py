from django.shortcuts import render
# Import category and product data from model
from .models import Product
from .models import Category


# View function 'all_products()'
def all_products(request):
    """ Show all products, applicable for sorting and search queries """

    # Variable 'categories' to store all available categories
    categories = Category.objects.all()

    # Variable 'products' to store all available data from imported Product model
    products = Product.objects.all()

    # Then store categories and products in 'context' as key value 
    # to make this data available
    context = {
        'products': products,
        'categories': categories,
    }

    # And define in which file the 'context' will be rendered in
    # products/templates/products/products.html
    return render(request, 'products/products.html', context)