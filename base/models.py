from datetime import datetime
from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Rental(TimeStampedModel):
    name = models.CharField(max_length=30)

class Reservation(TimeStampedModel):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE, null=False, blank=False)
    checkin = models.DateField()
    checkout = models.DateField()