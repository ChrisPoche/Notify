from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<id>\d+)/tolibrary$', views.addSongYourMusic),
    url(r'^search$', views.searchPage),
    url(r'^search_results', views.searchResult),
    url(r'^playlists$', views.playlists),
    url(r'^upload$', views.uploadpage),
    url(r'^checkfile$', views.checkfile)
]