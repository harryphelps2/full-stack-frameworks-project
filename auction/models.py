from django.db import models
from prints.models import Print

class Original(Print):
    highest_bid = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title
    