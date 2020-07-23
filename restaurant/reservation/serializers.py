from rest_framework import serializers

from .models import Reservation


class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            "id",
            "date",
            "duration",
            "number_of_guests",
            "phone_number",
            "email",
            "extra_information",
            "confirmed"
        )


