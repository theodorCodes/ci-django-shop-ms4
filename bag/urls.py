from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    # It's going to have a URL containing the item id.
    # Will return our add_to_bag view
    # And will be named add_to_bag.
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
]