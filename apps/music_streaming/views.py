# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login.models import User
from django.shortcuts import render, redirect
from models import Artist, Album, Track
from forms import UploadForm
from mutagen.mp3 import EasyMP3

import math
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

def uploadpage(request):
    context = {
        'uploadform': UploadForm()
    }
    return render(request, 'music_streaming/upload.html', context)

def checkfile(request):
    print "called checkfile"
    requestcopy = request.POST.copy()
    form = UploadForm(requestcopy)

    file = request.FILES['trackfile']
    easy = EasyMP3(file)

    form.data['artistname'] = easy['artist'][0]
    form.data['artistdesc'] = 'description'

    form.data['albumname'] = easy['album'][0]
    if 'date' in easy:
        form.data['albumyear'] = easy['date'][0]

    form.data['trackname'] = easy['title'][0]
    form.data['tracknumber'] = easy['tracknumber'][0][0]
    form.data['tracklength'] = int(math.ceil(easy.info.length))

    if 'confirmationbox' in form.data:
        print 'boxfull'
        createdatabaseentries(file, form)
        context = {
            'uploadform': form
        }
        return render(request, 'music_streaming/upload.html', context)

    else:
        context = {
            'uploadform': form
        }
        return render(request, 'music_streaming/upload.html', context)

def createdatabaseentries(file, form):
    print 'checking artist'
    if len(Artist.objects.filter(name=form.data['artistname'])) == False:
        artist = Artist.objects.create(name=form.data['artistname'], desc=form.data['artistdesc'])
        print'created artist'
    else:
        artist = Artist.objects.get(name=form.data['artistname'])

    print 'checking album'
    if len(Album.objects.filter(name=form.data['albumname'])) == False:
        album = Album.objects.create(name=form.data['albumname'], releaseyear=form.data['albumyear'])
        album.save()
        album.artists.add(artist)
        print 'created album'
    else:
        album = Album.objects.get(name=form.data['albumname'])

    track = Track.objects.create(title=form.data['trackname'], tracknumber=form.data['tracknumber'], length=form.data['tracklength'], location=file, album=album)
    track.save()
    print album.id
    print 'createdtrack'


