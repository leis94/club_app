"""Trips URLs."""

#Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

#Views
from .views import trips as trip_views


router = DefaultRouter()
router.register(r'trips', trip_views.TripViewSet, basename='trip')
router.register(
    r'users/(?P<id>\d+)/trips/create',
    
    trip_views.TripViewSet,
    basename='trip'
)

urlpatterns = [
    path('', include(router.urls))

]