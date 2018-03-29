# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login.models import User
from django.shortcuts import render

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

    }
    return 

def playlists(request, username):
    print "AJAX Playlists"
    context = {
    }
    return render(request, 'music_streaming/_your_music.html', context)