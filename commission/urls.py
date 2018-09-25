from django.urls import path, re_path
from .views import commission, request_submitted, awaiting_approval

urlpatterns = [
    path('', commission, name='commission'),
    path('submitted', request_submitted, name='request_submitted'),
    path('awaiting_approval', awaiting_approval, name='awaiting_approval'),
]