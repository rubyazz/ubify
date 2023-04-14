from django.contrib import admin
from .models import Singer, Album, Song, Like

admin.site.register(Singer)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Like)
