"""Users views."""

# Django REST Framework
from rest_framework import status
from rest_framework.views import APIView

# Serializers
from club_app.users.serializers import UserLoginSerializer

class UserLoginAPIView(APIView):
    """User login API View"""

    def post(self, request, *args, **kwargs):
        """ Handle HTTP POST request."""
        serializer = UserLoginSerializer(data=request.data)
        serializer = is_valid(raise_exception=True)
        token = serializer.save()
        data = {
            'user': 'hola',
            'access_token': token
        }
        return Reponse(data, status=status.HTTP_201_CREATED)