# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login.models import User
from django.shortcuts import render, redirect
from models import Artist, Album, Track

# Create your views here.

def index(request, username):
    user = User.objects.get(username = request.session['username'])
    context = {
        'user' : user
    }
    return render(request, 'music_streaming/index.html', context)

def searchPage(request, username):
    print "AJAX CONNECTED"
    if 'recent_searches' not in request.session:
        request.session['recent_searches'] = []
    recent_searches = request.session['recent_searches']
    context = {
        'recent_searches' : recent_searches
    }
    return render(request, 'music_streaming/_search.html', context)

def searchResult(request, method="POST"):
    result = request.POST['search_result']
    context = {
        'result' : result
    }
    return render(request, 'music_streaming/_search.html', context)

def playlists(request, username):
    print "AJAX Playlists"
    context = {
    }
    return render(request, 'music_streaming/_your_music.html', context)

def adddata(request, username, method='POST'):
    Artist.objects.create(
        name = request.POST['artist'],
        desc = request.POST['desc'],
    )
    Album.objects.create(
        name = request.POST['album'],
        releaseyear = request.POST['releaseyear'],
        interests = request.POST['interest']
    )
    album_id = Album.objects.get(name = 'Abbey Road')
    Track.objects.create(
        title = request.POST['track'],
        tracknumber = request.POST['tracknumber'],
        length = request.POST['length'],
        location = request.POST['location'],
        album_id = album_id.id
    )
    return redirect('/{}/playlists'.format(username))
    