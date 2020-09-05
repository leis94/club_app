"""Users URLs."""

#Django
from django.urls import path, include

#Views
from club_app.users.views import UserLoginAPIView

urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name='login')
]