# Imports available urls paths and views
from django.urls import path
from . import views


# Create list with routes and list
# 'all_products' view function and 'products' variable from views.py
# requires registration in project wide router in project_main/urls.py
urlpatterns = [
    path('', views.all_products, name='products'),  # Route for catalog view
    path('<product_id>', views.product_detail, name='product_detail'),  # Route for detail view
]