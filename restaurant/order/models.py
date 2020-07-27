from django.core.validators import MinValueValidator
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=100, blank=False)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.description}'


class Bill(models.Model):
    total_price = models.FloatField(default=0)
    description = models.TextField()
    active = models.BooleanField(default=True, auto_created=True)

    def __str__(self):
        return self.description


class Order(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.PROTECT)
    amount = models.PositiveIntegerField(null=False, validators=[MinValueValidator(1)])
    extra_information = models.TextField()

    def __str__(self):
        return f'{self.position} - {self.description}'
