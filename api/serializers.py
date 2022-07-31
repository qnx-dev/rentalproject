from rest_framework import serializers
from base.models import (
    Rental,
    Reservation,
)

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ('__all__')

class ReservationSerializer(serializers.ModelSerializer):
    rental = RentalSerializer(read_only=True)
    class Meta:
        model = Reservation
        fields = (
            'id',
            'checkin',
            'checkout',
            'rental',
        )