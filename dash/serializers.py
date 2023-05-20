from rest_framework import serializers

from users.models import CustomUser

from .models import *


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = "__all__"


class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True)

    class Meta:
        model = Singer
        fields = "__all__"


class GeneralSerializer(serializers.Serializer):
    singers = ArtistSerializer(many=True)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "img",
            "nickname",
            "email",
            "is_active",
            "is_singer",
            "is_listener",
        )
