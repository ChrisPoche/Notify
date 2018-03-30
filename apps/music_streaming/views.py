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

def addSongYourMusic(request, username, id):
    user = User.objects.get(id = request.session['id'])
    print user.username
    addsong = Track.objects.get(id=id)
    addsong.followers.add(user)
    addsong.save()
    return redirect('/{}/search_results'.format(user.username))