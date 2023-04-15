from rest_framework import generics
from rest_framework.response import Response
from .serializer import CustomUserRegistrationSerializer
from .models import CustomUser

class CustomUserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserRegistrationSerializer
