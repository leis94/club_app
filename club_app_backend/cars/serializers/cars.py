# Django REST Framework
from rest_framework import serializers

# Models
from club_app_backend.cars.models import Car


class CarModelSerializer(serializers.ModelSerializer):
    """Car model serializer."""

    class Meta:
        """Meta Class."""

        model = Car
        fields = '__all__'


    