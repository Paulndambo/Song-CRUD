from django.shortcuts import render
from .models import Song, Artiste, Lyric
# Create your views here.
def home(request):
    songs = Song.objects.all()
    context = {
        "songs": songs
    }
    return render(request, "songs.html", context)


def create_song(request):
    context = {

    }
    return render(request, "new-song.html", context)

def artists(request):
    context = {
        "artists": Artiste.objects.all()
    }
    return render(request, "artistes.html", context)


def create_artist(request):
    context = {

    }
    return render(request, "new-artiste.html", context)

def lyrics(request):
    context = {
        "lyrics": Lyric.objects.all()
    }
    return render(request, "lyrics.html", context)


def create_lyrics(request):
    context = {

    }
    return render(request, "new-lyrics.html", context)
