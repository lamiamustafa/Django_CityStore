from django.forms import modelform_factory
from django.shortcuts import render, redirect
from .models import User

# Create your views here.
from store.models import Product,User

def getAllProducts(request):
    products = Product.objects.all()
    return render(request, "products/getAll.html", {"products": products})

def product_details(request, id):
    product = Product.objects.get(pk=id)
    return render(request, "products/details.html", {"product": product})

UserForm = modelform_factory(User, exclude=[])

def user_register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Home")
    else:
        form = UserForm()
        return render(request, "users/register.html", {"form": form})
