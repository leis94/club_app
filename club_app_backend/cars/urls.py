"""Cars URLs."""

#Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

#Views
from .views import cars as car_views


router = DefaultRouter()
router.register(r'users', car_views.CarViewSet, basename='car')

urlpatterns = [
    path('', include(router.urls)),
    
]