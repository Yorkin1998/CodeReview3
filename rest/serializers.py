from rest_framework import serializers
from .models import Artist,Album,Music

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields="__all__"

class AlbumSerializer(serializers.ModelSerializer):
    related_artist=ArtistSerializer()
    class Meta:
        model = Album
        fields="__all__"

class MusicSerializer(serializers.ModelSerializer):
    artist=ArtistSerializer()
    album_name=AlbumSerializer()
    class Meta:
        model = Music
        fields="__all__"
