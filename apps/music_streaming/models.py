# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login.models import User

class Track(models.Model):
    title = models.CharField(max_length=255)
    tracknumber = models.IntegerField()
    length = models.IntegerField() # length in seconds
    location = models.FileField(upload_to='music/')
    interests = models.ManyToManyField(Interest, related_name='tracks')
    followers = models.ManyToManyField(User, related_name='follows')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Artist(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    followers = models.ManyToManyField(User, related_name='follows')
    artist_image = models.ImageField(upload_to='artistimages/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Album(models.Model):
    name = models.CharField(max_length=255)
    releaseyear = models.IntegerField(max_length=4)
    artists = models.ManyToManyField(Artist, related_name='artists')
    interests = models.ManyToManyField(InterestGenre, related_name='albums')
    album_image = models.ImageField(upload_to='albumimages/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Interest(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=1) # 'i' for instrument, 'g' for genre
    users = models.ManyToManyField(User, related_name='interests')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class InterestInstrument(models.Model):
    interest = models.OneToOneField(Interest, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class InterestGenre(models.Model):
    interest = models.OneToOneField(Interest, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playlistjson = models.TextField() # stored as JSON data - note https://docs.python.org/2/library/json.html#encoders-and-decoders
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
