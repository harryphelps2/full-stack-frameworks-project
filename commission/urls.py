from django.urls import path, re_path
from .views import commission_status, customer_submit_request, request_submitted, awaiting_approval, accept_proposal, awaiting_deposit, work_in_progress

urlpatterns = [
    path('', commission_status, name='commission_status'),
    path('customer_submit_request', customer_submit_request, name='customer_submit_request'),
    path('request_submitted', request_submitted, name='request_submitted'),
    path('awaiting_approval', awaiting_approval, name='awaiting_approval'),
    path('accept_proposal', accept_proposal, name='accept_proposal'),
    path('awaiting_deposit', awaiting_deposit, name='awaiting_deposit'),
    path('work_in_progress', work_in_progress, name='work_in_progress'),
]