from django.shortcuts import render

from kids.models import Kids

def home(request):
    kids = Kids.objects
    return render(request, 'kids/home.html', {'kids':kids})
