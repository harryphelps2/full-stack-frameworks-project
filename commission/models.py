from django.db import models
from django.contrib.auth.models import User

# Add null values to this model
class Commission(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=50, blank='False')
    details = models.TextField(blank='False')
    size = models.CharField(max_length=20, blank='False')
    price = models.DecimalField(max_digits=10, decimal_places=2, null="True")
    image = models.FileField(upload_to='media/commissions')
    proposed_date = models.DateField(blank=True, auto_now=False, auto_now_add=False)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)
    deposit_paid = models.BooleanField(default=False)
    deposit_date = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)
    in_progress = models.BooleanField(default=False)
    completed = models.BooleanField(default=False) 
    completed_date = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)
    fully_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
