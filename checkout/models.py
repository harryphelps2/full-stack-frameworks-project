from django.db import models
from prints.models import Print

class Order(models.Model):
    full_name = models.CharField(max_length=50, blank='False')
    address_line1 = models.CharField(max_length=100, blank='False')
    address_line2 = models.CharField(max_length=100, blank='True')
    county = models.CharField(max_length=30, blank='False')
    postcode = models.CharField(max_length=30, blank='True')
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
    

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null='False', on_delete=models.PROTECT)
    product = models.ForeignKey(Print, null='False', on_delete=models.PROTECT)
    quantity = models.IntegerField(blank='False')

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product, self.product.price)
    

