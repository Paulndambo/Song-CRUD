from rest_framework import serializers
from .models import Song, Artiste, Lyric

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        mdoel = Artiste
        fields = "__all__"


class SongSerializer(serializers.ModelSerializer):
    #artist = ArtisteSerializer()
    class Meta:
        model = Song
        fields = "__all__"


class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = "__all__"
