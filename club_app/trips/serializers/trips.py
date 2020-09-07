"""Trips serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from club_app.trips.models import Trip
from club_app.cars.models import Car
from club_app.users.models import User

# Serializers
from club_app.users.serializers import UserModelSerializer
from club_app.cars.serializers import CarModelSerialiser

# Utilities
from datetime import timedelta
from django.utils import timezone


class TripModelSerializer(serializers.ModelSerializer):
    """Trip model serializer."""
    
    passenger = UserModelSerializer(read_only=True)
    car = CarModelSerialiser(read_only=True)

    class Meta:
        """Meta class."""
        model = Trip
        fields = '__all__'
        read_only_fields = (
            'passenger',
            'car',
            'rating',
        )
    
        def update(self, instance, data):
        """ Allow updates only before departure date."""
        now = timezone.now()
        if instance.departure_date <= now:
            raise serializers.ValidationError('Ongoing trips cannot be modified.')
        return super(TripModelSerializer, self).update(instance, data)


class CreateTripSerializer(serializers.ModelSerializer):
    """Create trip serializer."""
    passenger = serializers.HiddenField(default=serializers.CurrentUserDefault())

    # driver = car.driver()


    class Meta:
        """Meta class."""
        model = Trip
        exclude = ('passenger','car', 'is_active')

    
    def create(self, data):
        """Create trip and update stats."""
        car = Car.objects.get(is_available=True).first()
        trip = Trip.objects.create(**data, car=car)

        # Car
        car.trips_taken += 1
        car.save()

        # User
        profile = data['passenger'].profile
        profile.trips_taken += 1
        profile.save()

        return ride


