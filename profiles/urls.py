from django.urls import path
from . import views

# url / view function / template
urlpatterns = [
    path('', views.profile, name='profile'),
    path('custom_products/', views.profile_custom_products, name='profile_custom_products'),
    path('custom_orders/', views.profile_custom_orders, name='profile_custom_orders'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('allorders/', views.order_overview, name='allorders'),
]