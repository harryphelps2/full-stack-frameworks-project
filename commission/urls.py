from django.urls import path, re_path
from .views import commission, awaiting_acceptance 

urlpatterns = [
    path('', commission, name='commission'),
    path('submitted', awaiting_acceptance, name='awaiting_acceptance')
]