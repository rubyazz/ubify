from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.permissions import IsAdminUser

from rest_framework import permissions
from .models import *
from .serializers import *


# Create your views here.
def main(request):
    return render(request, "index.html")


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
