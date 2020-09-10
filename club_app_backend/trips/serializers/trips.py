"""Trips serializers."""
# Django
from django.utils import timezone

# Django REST FRAMEWORK
from rest_framework import serializers

# Serializers
from club_app_backend.users.serializers import UserModelSerializer
from club_app_backend.cars.serializers import CarModelSerializer

# Models
from club_app_backend.trips.models import Trip
from club_app_backend.cars.models import Car

class TripModelSerializer(serializers.ModelSerializer):

    """Trip model serializer"""

    passenger = UserModelSerializer(read_only=True)
    requested_at = serializers.DateTimeField(source='created', read_only=True)

    class Meta:
        """Meta class."""

        model = Trip
        fields = '__all__'

    def create(self, data):
        """Create a new trip"""
        passenger = data['user']
        car = Car.objects.filter(is_available=True).first()
        # import pdb; pdb.set_trace()
        trip = Trip.objects.create(
            passenger=passenger,
            car=car,
            travel_time=data['travel_time'],
            distance = data['distance'],
            departure_location = data['departure_location'],
            arrival_location = data['arrival_location'],
        )
        return trip


#         return trip

# class RequestTripSerializer(serializers.Serializer):
#     """ Request a trip serializers.
    
#     User object must be provided in the context.
#     """

#     passenger = serializers.HiddenField(default=serializers.CurrentUserDefault())

#     def create(self, data):
#         """Create a new trip"""
#         passenger = data['user']
#         car = Car.objects.get(is_available=True).first()

#         trip = Trip.objects.create(
#             passenger=passenger,
#             car=car,
#         )

#         return trip


    
