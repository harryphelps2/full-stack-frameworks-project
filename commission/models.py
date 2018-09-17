from django.db import models
from django.contrib.auth.models import User

class Commission(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=50, blank='False')
    description = models.TextField(blank='False')
    size = models.CharField(max_length=20, blank='False')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank='False')
    image = models.ImageField(upload_to='img', height_field=None, width_field=None, max_length=None, blank='False')
    fully_paid = models.BooleanField()
    status = models.CharField(max_length=20, blank='False') 