from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
# Check access with login decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category, Type, Format
from .forms import ProductForm  # Import product form
from .forms import CustomProductForm  # Import product form


# Product catalog view function all_products()
def all_products(request):
    """ Show all products in catalog view, 
        applicable for sorting and search queries """

    # Variable 'categories' to store all available categories
    # except 'custom_product' from Django query set,
    # prevents showing custom product in catalog category menu
    # categories = Category.objects.exclude(name__in=['custom_product'])
    categories = Category.objects.all()

    # Variable 'products' stores all product names from model
    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
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



# Add custom product with configurable product template
def custom_product(request):
    """ Create custom product """

    if request.method == 'POST':
        # Create instance of product form from post including files
        form = CustomProductForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            product = form.save()
            messages.success(request, 'Successfully added product!')
            # return redirect(reverse('add_product'))
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        # Render empty instance of the form
        form = CustomProductForm(
            initial={
                'sku': 0,
                'name': 'Custom Artwork',
                'price': 0.00,
                'rating': 0,
            }
        )

    # Template
    template = 'products/custom_product.html'
    # Context for template
    context = {
        'form': form,
    }

    return render(request, template, context)



# Add Product form view
@login_required
def add_product(request):
    """ Add a product to the store """
    # Limit user access
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        # Create instance of product form from post including files
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            product = form.save()
            messages.success(request, 'Successfully added product!')
            # return redirect(reverse('add_product'))
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        # Render empty instance of the form
        form = ProductForm()

    # Template
    template = 'products/add_product.html'
    # Context for template
    context = {
        'form': form,
    }

    return render(request, template, context)


# Edit Product view
@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    # Limit user access
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    # Get product
    product = get_object_or_404(Product, pk=product_id)
    # If post
    if request.method == 'POST':
        # Make instance of product form with request product and request files
        form = ProductForm(request.POST, request.FILES, instance=product)
        # If form valid
        if form.is_valid():
            # Save
            form.save()
            # Response message
            messages.success(request, 'Successfully updated product!')
            # Redirect to product detail page with product id
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        # Make instance of product form with produkt
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')
    # Template to use
    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


# Delete products
@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    # Limit user access 
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    # Get product
    product = get_object_or_404(Product, pk=product_id)
    # Call product delete
    product.delete()
    # Response message
    messages.success(request, 'Product deleted!')
    # Redirect to products view
    return redirect(reverse('products'))