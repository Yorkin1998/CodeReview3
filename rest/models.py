from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class Artist(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name

class Album(models.Model):
    related_artist=models.ForeignKey(Artist,on_delete=models.CASCADE)
    album_name=models.CharField(max_length=255,null=True)
    release=models.DateField()
    def __str__(self) -> str:
        return self.album_name

class Music(models.Model):
    music_name=models.CharField(max_length=255,null=True)
    artist=models.ForeignKey(Artist,on_delete=models.CASCADE)
    album_name=ChainedForeignKey(Album,chained_field="artist",chained_model_field="related_artist",show_all=False,auto_choose=True,sort=True)
    def __str__(self) -> str:
        return self.music_name