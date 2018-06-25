from django.urls import path, include

from men import views


urlpatterns = [
    path('Men/', views.Men, name='Men'),
]