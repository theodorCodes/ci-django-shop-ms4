# Imports available urls paths and views
from django.urls import path
from . import views


# Create list with routes and list
# 'all_products' view function and 'products' variable from views.py
# requires registration in project wide router in project_main/urls.py
urlpatterns = [
    path('', views.all_products, name='products'),  # Route for catalog view
    # Route for detail view, specifying that id is an integer
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    # Points to add product view
    path('add/', views.add_product, name='add_product'),
    # Edit product page
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    # Delete products at products/delete/product_id
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]