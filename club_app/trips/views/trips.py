"""Trips view.s"""

# Django REST Framework
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

# Serializers
from club_app.trips.serializers import (
    RequestTripSerializer,
)

# Models
from club_app.cars.models import Car

# Utilities
from datetime import timedelta
from django.utils import timezone


class TripViewSet(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.RetrieveModelMixin,
                viewsets.GenericViewSet):
    """Ride view set."""


    # def dispatch(self, request, *args, **kwargs):
    #     """Verify that car is available."""
    #     is_available = kwargs['is_available']
    #     self.car = get_object_or_404(Car, is_available=True)
    #     return super(TripViewSet, self).dispatch(request, *args, **kwargs)

    def get_serializer_context(self):
        """Add car to serializer context."""
        context = super(TripViewSet, self).get_serializer_context()
        context['car'] = self.car
        return context


    def get_serializer_class(self):
        """Return serializer based on action."""
        if self.action == 'create':
            return CreateTripSerializer
        if self.action == 'update':
            return UpdateTripSerializer
        if self.action == 'finish':
            return EndTripSerializer
        return TripModelSerializer

    
    def get_queryset(self):
        """Return active cars ."""
            return self.car.filter(
                is_available=True,
            )
        return self.car.all()


    @action(detail=True, methods=['post'])
    def join(self, request, *args, **kwargs):
        """Add requesting user to trip."""
        trip = self.get_object()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(
            trip,
            data={'passenger': request.user.pk},
            context={'trip': trip, 'car':self.car},
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        trip = serializer.save()
        data = TripModelSerializer(trip).data
        return Response(data, status=status.HTTP_200_OK)


    @action(detail=True, methods=['post'])
    def finish(self, request, *args, **kwargs):
        """Call to finish a ride."""
        trip = self.get_object()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(
            trip,
            data = {'is_active': False, 'current_time': timezone.now()},
            context = self.get_serializer_context(),
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        trip = serializer.save()
        data = TripModelSerializer(trip).data
        return Response(data, status=status.HTTP_200_OK)