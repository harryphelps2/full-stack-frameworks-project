from django.shortcuts import render
from .models import Original

def originals(request):
    originals = Original.objects.all()
    return render(request, 'auction.html', { 'originals': originals })
