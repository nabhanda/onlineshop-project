from django.shortcuts import render

from men.models import Men

def men(request):
    men = Men.objects
    return render(request, 'men/home.html', {'men':men})