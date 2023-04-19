from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import AlbumAPIList, ArtistAPIList, SongAPIList

urlpatterns = [
    path("", views.hello, name="hello"),
    path("artists/list/", ArtistAPIList.as_view()),
    path("albums/list/", AlbumAPIList.as_view()),
    path("songs/list/", SongAPIList.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
