from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Singer, Album, Song
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer


class SingerViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.artist = Singer.objects.create(name="John Doe")

    def test_artist_list_view(self):
        response = self.client.get(reverse("artist_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.artist.name)

    def test_artist_detail_view(self):
        response = self.client.get(reverse("artist_detail", args=[self.artist.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.artist.name)

    def test_artist_create_view(self):
        response = self.client.post(reverse("artist_create"), {"name": "Jane Doe"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Singer.objects.last().name, "Jane Doe")

    def test_artist_update_view(self):
        response = self.client.post(reverse("artist_update", args=[self.artist.id]), {"name": "Jack Smith"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Singer.objects.get(id=self.artist.id).name, "Jack Smith")

    def test_artist_delete_view(self):
        response = self.client.post(reverse("artist_delete", args=[self.artist.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Singer.objects.filter(id=self.artist.id).exists())



class AlbumAPITestCase(APITestCase):
    def setUp(self):
        self.album1 = Album.objects.create(name="Album 1")
        self.album2 = Album.objects.create(name="Album 2")

    def test_list_albums(self):
        url = reverse("album-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_album(self):
        url = reverse("album-list")
        data = {"name": "Album 3"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Album 3")
        self.assertTrue(Album.objects.filter(name="Album 3").exists())


class SongAPITestCase(APITestCase):
    def setUp(self):
        self.album1 = Album.objects.create(name="Album 1")
        self.song1 = Song.objects.create(name="Song 1", album=self.album1)
        self.song2 = Song.objects.create(name="Song 2", album=self.album1)

    def test_list_songs(self):
        url = reverse("song-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_song(self):
        url = reverse("song-list")
        data = {"name": "Song 3", "album": self.album1.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Song 3")
        self.assertTrue(Song.objects.filter(name="Song 3").exists())
        self.assertEqual(Song.objects.filter(album=self.album1).count(), 3)