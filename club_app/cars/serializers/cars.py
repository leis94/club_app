"""Cars serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from club_app.cars.models import Car


class CarModelSerialiser(serializers.ModelSerializer):
    """Car model serializer."""

    class Meta:
        """Meta class."""

        model = Car
        fields = (
            'license',
            'manufactured',
            'brand_type',
            'model_year',
            'color',
            'driver',
        )