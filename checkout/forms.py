from django import forms
from .models import Order

class MakePaymentForm(forms.Form):
    
    MONTH_CHOICES = [(i, i) for i in range(1, 12+1)]
    YEAR_CHOICES = [(i, i) for i in range(2018, 2036)]
    
    credit_card_number = forms.CharField(label="Card number", required=False)
    cvv = forms.CharField(label='CVC number', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'address_line1', 'address_line2', 'county', 'postcode')
