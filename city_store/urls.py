"""city_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path
from home.views import home
from store.views import getAllProducts, product_details, user_register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='Home'),
    path('home', home, name='Home'),
    path('products', getAllProducts, name='Products'),
    path('products/<int:id>', product_details, name="details"),
    path('user_register', user_register, name='Register'),
]
