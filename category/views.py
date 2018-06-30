from django.shortcuts import render, get_object_or_404

from .models import *


def home(request):
    cat = Category.objects
    return render(request, 'category/home.html', {'cat':cat})


def subcategory(request):
    subcategory = Subcategory.objects
    return render(request, 'category/subcategory.html', {'subcategory':subcategory})

def product_list(request, category_slug=None):
    subcategory = None
    subcategories = Subcategory.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'category/productlist.html', {'subcategory':subcategory, 'subcategories':subcategories, 'products':products})