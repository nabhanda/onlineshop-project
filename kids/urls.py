from django.urls import path, include
from kids import views

urlpatterns = [
    path('', views.home, name='home'),
]