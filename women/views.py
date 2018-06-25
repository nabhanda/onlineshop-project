from django.shortcuts import render

from women.models import Women

def home(request):
    women = Women.objects
    return render(request, 'women/home.html', {'women':women})