from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import *


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"
