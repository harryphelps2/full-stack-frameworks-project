from django.shortcuts import render
from .forms import CommissionRequestForm
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Commission
from checkout.forms import MakePaymentForm
from django.conf import settings
from django.contrib import messages
import stripe
from django.template.context_processors import csrf

stripe.api_key = settings.STRIPE_SECRET

@login_required
def commission_status(request):
    """
    Commission form, customer fills in details for request and submits.
    Creates new entry for inspection and acceptance by artist.
    Redirect to proposal submitted if already have a commission.
    else if accepted = false redirect to awaiting approval
    else if accepted = true redirect to pay deposit
    else if deposit_paid = true redirect to work in progress
    Or work in progress if needed
    """
    # add logic so that if there is already a commission in progress it doesn't let you see this page
    user = request.user
    #need to convert this into an object I think instead of query set
    try:
        current_commission = Commission.objects.get(user=user)
        if not current_commission.price:
            return redirect(reverse('request_submitted'))
        elif not current_commission.price:
            return redirect(reverse('awaiting_approval'))
        elif not current_commission.deposit_paid: 
            return redirect(reverse('pay_deposit'))
        elif not current_commission.completed:
            return redirect(reverse('work_in_progress'))
        elif not current_commission.fully_paid: 
            return redirect(reverse('pay_full_amount'))
        else:
            return render (request, 'submit_proposal.html', {'commission_proposal_form':commission_proposal_form}) 
    except:
        commission_proposal_form = CommissionRequestForm()
        return render (request, 'submit_proposal.html', {'commission_proposal_form':commission_proposal_form})
        # # if not current_commission.accepted:
        # return redirect(reverse('request_submitted'))
        
    

@login_required
def customer_submit_request(request):
    if request.method=='POST':
        commission_proposal_form = CommissionRequestForm(request.POST)
        if commission_proposal_form.is_valid():
            commission_proposal = commission_proposal_form.save(commit=False)
            commission_proposal.proposed_date =  timezone.now()
            commission_proposal.user = request.user
            commission_proposal.save()
            return redirect(reverse('request_submitted'))
    else:
        commission_proposal_form = CommissionRequestForm()
    return render (request, 'submit_proposal.html', {'commission_proposal_form':commission_proposal_form})
        


@login_required
def request_submitted(request):
    """
    Shows view of proposal and waiting meme. Artist can though then upload
    image of small study and price so customer can look at decide whether 
    to accept or not. Artist then updates the price on django admin. 
    """
    user = request.user
    request_submitted = get_object_or_404(Commission, user=user)
    if not request_submitted.price:
        return render(request, 'request_submitted.html', {'request_submitted':request_submitted})
    else:
        return redirect(reverse('awaiting_approval'))    

@login_required
def awaiting_approval(request):
    """
    Shows price and study picture from artist for customer approval. Then customer needs to approve.
    """
    user = request.user
    awaiting_approval = get_object_or_404(Commission, user=user)
    return render(request, 'awaiting_approval.html', {'awaiting_approval':awaiting_approval})

@login_required
def accept_proposal(request):
    """
    View to update database when proposal is accepted.
    Add 10%of price to cart and redirect to cart.
    """
    user = request.user
    if request.method == 'POST':
        print(request.POST)
        accepted_commission = get_object_or_404(Commission, user=user)
        print(accepted_commission)
        accepted_commission.accepted = True
        accepted_commission.accepted_date = timezone.now()
        accepted_commission.save()
        """
        Redirect here to add deposit to cart as half of the price.

        """
        return redirect(reverse('pay_deposit'))

@login_required
def pay_deposit(request):
    """
    Page to pay the deposit.
    """
    user = request.user
    commission = get_object_or_404(Commission, user=user)
    price = commission.price
    deposit = float(commission.price) * 0.15
    """
    Add the code from all the checkout page. This should be its own checkout page
    and then up date deposit.paid to true
    """

    if request.method=='POST':
        payment_form = MakePaymentForm(request.POST)
        if payment_form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount = int(deposit * 100),
                    currency = "EUR",
                    description = request.user.email,
                    source = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            if customer.paid:
                messages.success('You have paid! Thank you')
                cart = {}
                return redirect(reverse('pay_deposit'))
            else:
                messages.error(request, "We were unable to take payment")
        else:
            messages.error(request, payment_form.errors)
    else:
        payment_form = MakePaymentForm()
    return render(request, 'pay_deposit.html', {'pay_deposit':pay_deposit, 'payment_form':payment_form, 'publishable':settings.STRIPE_PUBLISHABLE })

@login_required
def work_in_progress(request):
    """
    View to show the customer how the piece is coming along
    feedback model
    """
    return render(request, 'work_in_progress.html')

@login_required
def pay_full_amount(request):
    pass
                    

