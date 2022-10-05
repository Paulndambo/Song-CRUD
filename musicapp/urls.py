from django.urls import path
from .import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create-song/", views.create_song, name="create-song"),
    path("artists/", views.artists, name="artists"),
    path("create-artist/", views.create_artist, name="create-artist"),
    path("lyrics/", views.lyrics, name="lyrics"),
    path("create-lyrics/", views.create_lyrics, name="create-lyrics")
]