from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from .forms import MakePaymentForm, OrderForm
from django.conf import settings
from django.contrib import messages
import stripe
from django.template.context_processors import csrf
from .models import Print

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):

    if request.method=='POST':
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Print, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order = order,
                    product = product,
                    quantity = quantity
                )
                order_line_item.save()
            
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    source = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            if customer.paid:
                messages.success('You have paid! Thank you')
                cart = {}
                return redirect(reverse('prints'))
            else:
    # return a message to say we were unable to take a payment
                messages.error(request, "We were unable to take payment")
    #
    # else
        else:
    # print the payment form error
            print(order_form.is_valid())
            print(payment_form.is_valid())
            print(request.user.email)
            print(payment_form.errors)

    # send message saying we were unable to take a payment
            messages.error(request, payment_form.errors)
    # else
    else:
    # return empty payment and order form
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    # return rendered checkout.html wirth orderform, payment form and stripe publishable
    return render(request, 'checkout.html', {'order_form':order_form, 'payment_form':payment_form, 'publishable':settings.STRIPE_PUBLISHABLE})
