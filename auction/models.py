from django.db import models
from prints.models import Print
from django.contrib.auth.models import User

class Original(Print):
    highest_bidder = models.ForeignKey(User, null="True", on_delete=models.PROTECT)
    highest_bid = models.IntegerField()
    bid_time = models.DateTimeField(auto_now=False, auto_now_add=False, null="True")
    start_date_time = models.DateTimeField(null="True", auto_now=False, auto_now_add=False)
    end_date_time = models.DateTimeField(null="True", auto_now=False, auto_now_add=False)
    paid = models.BooleanField(default="False")

    def __str__(self):
        return self.title

