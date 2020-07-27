from django.contrib import admin
from .models import Position, Order, Bill

admin.site.register(Position)
admin.site.register(Bill)
admin.site.register(Order)