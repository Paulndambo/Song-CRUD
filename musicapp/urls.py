from django.urls import path, include
from .import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("songs-list", views.SongModelViewSet, basename="songs-list")
router.register("artists-list", views.ArtisteModelViewSet, basename="artists-list"),
router.register("lyrics-list", views.LyricModelViewSet, basename="lyrics-list")

urlpatterns = [
    path("", views.home, name="home"),
    path("create-song/", views.CreateSong.as_view(), name="create-song"),
    path("song/<int:pk>/", views.UpdateSong.as_view(), name="update-song"),
    path("song/delete/<int:id>/", views.delete_song, name="delete-song"),
    path("artists/", views.artists, name="artists"),
    path("create-artist/", views.CreateArtiste.as_view(), name="create-artist"),
    path("artiste/<int:pk>/", views.UpdateArtiste.as_view(), name="update-artiste"),
    path("artist/<int:id>/", views.delete_artiste, name="delete-artiste"),
    path("lyrics/", views.lyrics, name="lyrics"),
    path("create-lyrics/", views.CreateLyRics.as_view(), name="create-lyrics"),
    path("lyrics/<int:pk>/", views.UpdateLyrics.as_view(), name="update-lyrics"),
    path("lyrics/delete/<int:id>/", views.delete_lyrics, name="delete-lyrics"),
    #APIs Routes
    path("api/", include(router.urls)),
]