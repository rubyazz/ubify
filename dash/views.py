from django.db.models import Prefetch
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import filters, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


# Create your views here.
def main(request):
    return render(request, "index.html")


def home(request):
    return render(request, "home.html")


def hello(request):
    return JsonResponse({"Welcome to": "Ubify Api!"})


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow read permissions to anyone, including unauthenticated users
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if user is admin
        return (
            request.user and request.user.is_authenticated and request.user.is_superuser
        )


class ArtistAPIList(generics.ListCreateAPIView):
    queryset = Singer.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ["name", "nickname"]
    filter_backends = (filters.SearchFilter,)


class AlbumAPIList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = [
        "name",
    ]
    filter_backends = (filters.SearchFilter,)


class SongAPIList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = [
        "name",
    ]
    filter_backends = (filters.SearchFilter,)


class GeneralAPI(APIView):
    def get(self, request):
        singers = Singer.objects.all()
        serializer = GeneralSerializer({"singers": singers})
        return Response(serializer.data)
