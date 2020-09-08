"""Users URLs."""

#Django
from django.urls import path, include

#Views
from club_app_backend.users.views import (
    UserLoginAPIView, 
    UserSignUpAPIView,
)

urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name='login'),
    path('users/signup/', UserSignUpAPIView.as_view(), name='signup'),
]

