from django.core.validators import MinValueValidator
from django.db import models


class Reservation(models.Model):
    date = models.DateTimeField(null=False)
    duration = models.PositiveIntegerField(null=False, validators=[MinValueValidator(1)])
    number_of_guests = models.PositiveIntegerField(null=False, validators=[MinValueValidator(1)])
    phone_number = models.CharField(null=False, max_length=9)
    email = models.EmailField(null=False)
    extra_information = models.TextField(blank=True, null=True)
    confirmed = models.BooleanField(default=False, auto_created=False)

    def __str__(self):
        return f"{self.date} | {self.duration}h | {self.number_of_guests} person"
