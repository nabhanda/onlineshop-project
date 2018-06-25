from django.shortcuts import render, get_object_or_404

from .models import Category

def home(request):
    cat = Category.objects
    return render(request, 'category/home.html', {'cat':cat})

# def catego(request):
#     detailcat = get_object_or_404(Category, pk=cat_id)
#     return render(request, 'category/home.html', {'blog':detailcat})