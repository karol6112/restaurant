from rest_framework import serializers
from .models import Position, Order, Bill


class PositionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = (
            "id",
            "name",
            "price",
            "description"
        )


class BillSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = (
            'id',
            'description',
            'active',
            'total_price'
        )


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'bill',
            'position',
            'amount',
            'extra_information',
        )
