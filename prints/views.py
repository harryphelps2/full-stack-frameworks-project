from django.shortcuts import render
from .models import Prints

def all_prints(request):
    prints = Prints.objects.all()
    return render (request, 'prints.html', {'prints': prints})
