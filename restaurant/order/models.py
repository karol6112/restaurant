import decimal

from django.core.validators import MinValueValidator
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name} - {self.description}'


class Bill(models.Model):
    description = models.TextField(blank=False)
    active = models.BooleanField(default=True, auto_created=True)

    def __str__(self):
        return self.description

    def total_price(self):
        orders = self.order_bill.all()
        total_price = decimal.Decimal(0.00)
        for order in orders:
            amount = order.amount
            price = order.position.price
            total_price += amount * price
        return total_price


class Order(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name="order_bill")
    position = models.ForeignKey(Position, on_delete=models.PROTECT, related_name="order_position")
    amount = models.PositiveIntegerField(null=False, validators=[MinValueValidator(1)])
    extra_information = models.TextField(blank=True)

    def __str__(self):
        return f'{self.position} - {self.extra_information}'
