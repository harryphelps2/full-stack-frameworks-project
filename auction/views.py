from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from .models import Original
from django.contrib import messages
from datetime import datetime

def originals(request):
    originals = Original.objects.all()
    return render(request, 'auction.html', { 'originals': originals })

@login_required
def submit_bid(request, id):
    """
    Make bid model
    arrows to increase the current price and submit to the database overwriting 
    the current highest bid and current highest bid user
    1. Add highest bid to lido and display it under the picture
    2. have arrows either side that increase the price in £5 increments
    3. Submit button that takes the new amount and overwrites the highest bidder amount
    """ 
    original = get_object_or_404(Original, pk=id)
    old_bid = int(original.highest_bid)
    new_bid = int(request.POST.get('bid'))
    if new_bid >= old_bid:
        original.highest_bid = new_bid
        original.highest_bidder = request.user
        original.bid_time = datetime.now()
        original.save()
    else:
        messages.error(request, "You're not going to win the auction with that attitude")
    return redirect(reverse(originals))

# login required
def close_auction(request, id):
    """
    When now is larger than the closing time and date of the auction
    add the orginal to cart so it can go through checkout
    Have bool on the originals for paid and if it is paid then null the auction start and end date
    """
    pass