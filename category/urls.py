from django.urls import path, include, re_path

from category import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subcategory', views.subcategory, name='subcategory'),
    re_path(r'^()/$', views.subcategory, name='subcategory'),
    path('product', views.product_list, name='product'),
#add the product details page data here

]