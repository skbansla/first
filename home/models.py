from django.db import models

# Create your models here.
class Song(models.Model):
    artist = models.CharField(max_length=250)
    song_title = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    logo = models.CharField(max_length=3000)
