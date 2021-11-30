# Imports available urls paths and views
from django.urls import path
from . import views


# Create list with routes and list
# 'all_products' view function and 'products' variable from views.py
# Requires registration in project wide router in project_main/urls.py
urlpatterns = [
    path('', views.all_products, name='products'),
]