"""Cars views."""

# Django REST Framework
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from club_app_backend.cars.models import Car

# Serializers
from club_app_backend.cars.serializers import (
    CarModelSerializer,
#     UserLoginSerializer,
#     UserSignUpSerializer,
)


class CarViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):

    queryset = Car.objects.all()
    serializer_class = CarModelSerializer