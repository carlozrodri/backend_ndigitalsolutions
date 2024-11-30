from rest_framework import generics, permissions
from tasks.serializers import UserSerializer
from django.contrib.auth.models import User


class RegisterView(generics.CreateAPIView):
    """
    API view to register a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

