from django.shortcuts import render
from .forms import CommissionRequestForm
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Commission


@login_required
def commission(request):
    """
    Commission form, customer fills in details for request and submits.
    Creates new entry for inspection and acceptance by artist.
    """
    # add logic so that if there is already a commission in progress it doesn't let you see this page
    if request.method=='POST':
        commission_proposal_form = CommissionRequestForm(request.POST)
        if commission_proposal_form.is_valid():
            commission_proposal = commission_proposal_form.save(commit=False)
            commission_proposal.proposed_date =  timezone.now()
            commission_proposal.user = request.user
            commission_proposal.save()
            return redirect(reverse('awaiting_acceptance'))
    else:
        commission_proposal_form = CommissionRequestForm()
    return render (request, 'submit_proposal.html', {'commission_proposal_form':commission_proposal_form})

@login_required
def request_submitted(request):
    """
    Shows view of proposal and waiting meme. Artist can though then upload
    image of small study and price so customer can look at decide whether 
    to accept or not. 
    """
    user = request.user
    request_submitted = Commission.objects.filter(accepted_date=None, price=None, user=user)
    return render(request, 'request_submitted.html', {'request_submitted':request_submitted})

@login_required
def awaiting_approval(request):
    """
    Shows price and study picture from artist for customer approval.
    """
    awaiting_approval = Commission.objects.filter(accepted_date=None)
    return render(request, 'awaiting_approval.html', {'awaiting_approval':awaiting_approval})
