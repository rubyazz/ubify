from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import ArtistAPIList, AlbumAPIList, SongAPIList


urlpatterns = [
    path("", views.main, name="main"),
    path("artists/list/", ArtistAPIList.as_view()),
    path("albums/list/", AlbumAPIList.as_view()),
    path("songs/list/", SongAPIList.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
