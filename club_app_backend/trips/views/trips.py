"""Trip views."""

# Django REST Framework
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated

# Serializers
from club_app_backend.trips.serializers.trips import TripModelSerializer

# Models
from club_app_backend.trips.models import Trip

class TripViewSet(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet):
    "Trip view set."

    queryset = Trip.objects.all()
    serializer_class = TripModelSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        trip = serializer.save(user=self.request.user)


    # def get_permissions(self):
    #     """Assign permissions based on actions."""
    #     if self.action in ["list", "create", "update", "partial_update"]:
    #         permissions = [IsAuthenticated]
    #     return [permission() for permission in permissions]


    def destroy(self, instance):
        """Disable trip."""
        instance.is_active = False
        instance.save()


    # def create(self, request, *args, **kwargs):
    #     serializer = RequestTripSerializer(
    #         data=request.data,
    #         # context={'user': self.user, 'request': request}
    #     )
    #     serializer.is_valid(raise_exception=True)
    #     trip = serializer.save()

    #     data = self.get_serializer(trip).data
    #     return Response(data, status=status.HTTP_201_CREATED)