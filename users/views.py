from rest_framework import generics

from .models import CustomUser
from .serializer import CustomUserRegistrationSerializer


class CustomUserRegistrationView(generics.CreateAPIView):
    """
    Модуль представлений пользователей
    """

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserRegistrationSerializer
