from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category



# Product catalog view function all_products()
def all_products(request):
    """ Show all products in catalog view, 
        applicable for sorting and search queries """

    # Variable 'categories' to store all available categories
    categories = Category.objects.all()
    # Variable 'products' stores all available data from imported Product model
    products = Product.objects.all()
    query = None


    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)



    # Then store categories and products in 'context' as key value 
    # making this data available in products.html
    context = {
        'products': products,
        'search_term': query,
        'categories': categories,
    }

    # And define in which file the 'context' will be rendered in
    # products/templates/products/products.html
    return render(request, 'products/products.html', context)


# Product detail view function product_detail()
def product_detail(request, product_id):
    """ Show product detail view """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)