from rest_framework import generics
from .serializer import CustomUserRegistrationSerializer
from .models import CustomUser


class CustomUserRegistrationView(generics.CreateAPIView):
    """
    Модуль представлений пользователей
    """

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserRegistrationSerializer
