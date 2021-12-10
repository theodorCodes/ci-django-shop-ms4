"""project_main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Allauth requires 'include'
from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Imports from settings.py
from django.conf.urls.static import static  # Import links to static files

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), # Required by Allauth
    path('', include('home.urls')),  # Including home view routing
    path('products/', include('products.urls')),  # Including products/urls.py
    path('bag/', include('bag.urls')),  # Including bag/urls.py
    path('checkout/', include('checkout.urls')),  # Including checkout/urls.py
    path('profile/', include('profiles.urls')),  # Including profiles/urls.py
]

# Path to media folder
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)