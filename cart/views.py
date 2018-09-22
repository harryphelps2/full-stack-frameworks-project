from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from datetime import datetime
from auction.models import Original

def view_cart(request):
    """
    Shows cart contents
    """
    user = request.user
    now = datetime.now()
    auction_items_to_be_paid = Original.objects.filter(end_date_time__gte=now, paid=False, highest_bidder=user)
    return render(request, "cart.html", {'auction_items_to_be_paid':auction_items_to_be_paid})

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