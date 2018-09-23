from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from .models import Original
from django.contrib import messages
from datetime import datetime

def originals(request):
    now = datetime.now()
    originals = Original.objects.all().filter(end_date_time__gte=now)
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
    old_bid = original.highest_bid
    new_bid = float(request.POST.get('bid'))
    if new_bid >= old_bid:
        original.highest_bid = float(new_bid)
        original.highest_bidder = request.user
        original.bid_time = datetime.now()
        original.save()
    else:
        messages.error(request, "You're not going to win the auction with that attitude")
    return redirect(reverse(originals))

# login required
def you_win(request):
    """
    When now is larger than the closing time and date of the auction
    add the orginal to cart so it can go through checkout
    Have bool on the originals for paid and if it is paid then null the auction start and end date
    Background tasks
    https://django-background-tasks.readthedocs.io/en/latest/
    filter originals by paid is false and auction is closed
    append to list


    on cart paid show separate auction originals 
    add to list
    add item to cart
    """
    # filter originals by paid is false and auction is closed
    now = datetime.now()
    auction_items_to_be_paid = Original.objects.exclude(end_date_time__lte=now, paid="True")
    if not auction_items_to_be_paid:
        redirect(reverse(originals)) 
    # if it is empty, then redirect to auctions.html

    return render(request, 'youwin.html', { 'auction_items_to_be_paid': auction_items_to_be_paid }) 