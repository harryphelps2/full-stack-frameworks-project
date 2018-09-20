from django.db import models
from prints.models import Print
from django.contrib.auth.models import User

class Original(Print):
    highest_bidder = models.ForeignKey(User, null="True", on_delete=models.PROTECT)
    highest_bid = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField(null="True")
    end_date = models.DateField(null="True")
    paid = models.BooleanField(null="True")

    def __str__(self):
        return self.title

