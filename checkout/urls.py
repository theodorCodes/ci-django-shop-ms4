# This file requires url registration in project_main/urls.py
from django.urls import path  # Import url path
from . import views  # Import views


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
]