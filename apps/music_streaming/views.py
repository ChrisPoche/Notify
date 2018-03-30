# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login.models import User
from django.shortcuts import render, redirect
from models import Artist, Album, Track
from forms import UploadForm

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

def searchResult(request, username, method="POST"):
    print "KEYSTROKE RECORDED!!!"
    result = request.POST['search_result']
    print request.POST['search_result']
    if len(result):
        album_search = Album.objects.filter(name__icontains = request.POST['search_result'])
    else:
        album_search = []
    album_search = sorted(album_search)
    album_search = album_search[0:10]
    if len(result):
        artist_search = Artist.objects.filter(name__icontains = request.POST['search_result'])
    else:
        artist_search = []
    artist_search = sorted(artist_search)
    artist_search = artist_search[0:10]
    if len(result):
        track_search = Track.objects.filter(title__icontains = request.POST['search_result'])
    else:
        track_search = []
    track_search = sorted(track_search)
    track_search = track_search[0:10]
    if len(result):
        user_search_first = User.objects.filter(first_name__icontains = request.POST['search_result']).exclude(id=request.session['id'])
        user_search_last = User.objects.filter(last_name__icontains = request.POST['search_result']).exclude(id=request.session['id'])
        user_search_username = User.objects.filter(username__icontains = request.POST['search_result']).exclude(id=request.session['id'])
    else:
        user_search_first = []
        user_search_last = []
        user_search_username = []
    user_search_first = sorted(user_search_first)
    user_search_first = user_search_first[0:10]
    user_search_last = sorted(user_search_last)
    user_search_last = user_search_last[0:10]
    user_search_username = sorted(user_search_username)
    user_search_username = user_search_username[0:10]
    for track in track_search:
        minutes = track.length/60
        if track.length%60 < 10:
            seconds = '0{}'.format(track.length%60)
        else:
            seconds = track.length%60
        track.length = '{}:{}'.format(minutes,seconds)
        print "************ TRACK SEARCH ************",track.length
    context = {
        'result' : result,
        'album_search' : album_search,
        'artist_search' : artist_search,
        'track_search' : track_search,
        'user_search_first' : user_search_first,
        'user_search_last' : user_search_last,
        'user_search_username' : user_search_username,
    }
    return render(request, 'music_streaming/_search_results.html', context)

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

def addSongYourMusic(request, username, id):
    user = User.objects.get(id = request.session['id'])
    print user.username
    print id
    addsong = Track.objects.get(id=id)
    addsong.followers.add(user)
    addsong.save()
    return redirect('/{}/'.format(user.username))