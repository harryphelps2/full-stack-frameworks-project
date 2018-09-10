from django.shortcuts import render
from .models import Print

def all_prints(request):
    prints = Print.objects.all()
    return render (request, 'prints.html', {'prints': prints})


