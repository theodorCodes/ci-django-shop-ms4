from django.contrib import admin
from django.urls import path
from . import views

# Home view routing
urlpatterns = [
    path('', views.index, name='home')
]