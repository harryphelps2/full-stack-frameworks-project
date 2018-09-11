from django.shortcuts import render

def view_cart(request):
    """shows cart contents"""
    return render(request, 'cart.html')


