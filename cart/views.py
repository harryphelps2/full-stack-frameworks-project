from django.shortcuts import render, redirect, reverse
from django.contrib import messages

def view_cart(request):
    """shows cart contents"""
    return render(request, "cart.html")

def add_to_cart(request, id):
    """Add quantity of product to the cart"""
    quantity = int(request.POST.get('quantity'))    

    # Get the current cart or start a new one
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    messages.success(request, "Item added to cart")
    return redirect(reverse('prints'))

def adjust_cart(request, id):
    quantity = int(request.POST.get('new_quantity'))
    cart = request.session.get('cart', {}) 

    if quantity > 0:
       cart[id] = quantity 
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))    