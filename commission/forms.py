from django import forms
from .models import Commission, Feedback

class CommissionRequestForm(forms.ModelForm):
    title = forms.CharField(max_length=50, required=True) 
    details = forms.CharField(widget=forms.Textarea)
    size = forms.ChoiceField(choices=[("Small","30cm x 30cm"),
                                        ("Medium", "50cm x 50cm"),
                                        ("Large", "120 cm x 120cm"),
                                        ("Extra-Large", "200cm x 200cm")], required=True)
    image = forms.FileField(required=False)

    class Meta:
        model = Commission
        fields = ['title','details','size','image']

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ['comments']
