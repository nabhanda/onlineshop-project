from django.urls import path, include
from men import views

urlpatterns = [
    path('', views.men, name='home'),
]