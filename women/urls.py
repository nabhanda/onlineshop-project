from django.urls import path, include
from women import views

urlpatterns = [
    path('', views.home, name='home'),
]


