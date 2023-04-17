from django.contrib import admin

from .models import Album, Like, Singer, Song


@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "nickname",
        "img",
    )  # Specify fields to be displayed in the list view
    list_filter = ("name",)  # Add filters for filtering the list view
    search_fields = (
        "name",
        "nickname",
    )  # Add search fields for searching the list view
    ordering = ("name",)  # Specify the default sorting order


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("name", "singer", "img")
    list_filter = ("singer",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("name", "album", "time", "img")
    list_filter = ("album",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "song")
    list_filter = ("user",)
    search_fields = ("user__username",)
    ordering = ("user",)
