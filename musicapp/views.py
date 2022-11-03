<<<<<<< HEAD
from django.shortcuts import render
=======
from django.shortcuts import render, redirect
from .models import Song, Artiste, Lyric
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.http import HttpResponseRedirect

>>>>>>> Week5Task
# Create your views here.
def home(request):
    songs = Song.objects.all()
    context = {
        "songs": songs
    }
    return render(request, "songs.html", context)



class CreateSong(CreateView):
    model = Song
    fields = "__all__"
    template_name = "new-song.html"

class UpdateSong(UpdateView):
    model = Song
    fields = "__all__"
    template_name = "update-song.html"


def delete_song(request, id):
    song = Song.objects.get(pk=id)
    song.delete()
    return redirect("/")


def artists(request):
    context = {
        "artists": Artiste.objects.all()
    }
    return render(request, "artistes.html", context)

class CreateArtiste(CreateView):
    model = Artiste
    fields = "__all__"
    template_name = "new-artiste.html"

class UpdateArtiste(UpdateView):
    model = Artiste
    fields = "__all__"
    template_name = "update-artiste.html"

def delete_artiste(request, id):
    artist = Artiste.objects.get(pk=id)
    artist.delete()
    return redirect("/artists")


def lyrics(request):
    context = {
        "lyrics": Lyric.objects.all()
    }
    return render(request, "lyrics.html", context)


class CreateLyRics(CreateView):
    model = Lyric
    fields = "__all__"
    template_name = "new-lyrics.html"


class UpdateLyrics(UpdateView):
    model = Lyric
    fields = "__all__"
    template_name = "update-lyrics.html"

def delete_lyrics(request, id):
    lyric = Lyric.objects.get(pk=id)
    lyric.delete()
    return redirect("/lyrics")