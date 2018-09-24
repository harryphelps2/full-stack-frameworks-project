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
def awaiting_acceptance(request):
    """
    Shows view of proposal and waiting meme. Artist can though then upload
    image of small study and price so customer can look at decide whether 
    to accept or not. 
    """
    user = request.user
    commission_awaiting_acceptance = Commission.objects.filter(accepted_date=None)
    print(commission_awaiting_acceptance)
    return render(request, 'awaiting_acceptance.html', {'commission_awaiting_acceptance':commission_awaiting_acceptance})

