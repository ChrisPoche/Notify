# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Interest, InterestInstrument, InterestGenre, Track, Artist, Album, Playlist

admin.site.register(Interest)
admin.site.register(InterestInstrument)
admin.site.register(InterestGenre)
admin.site.register(Track)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Playlist)