from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^search$', views.searchPage),
    url(r'^search_results', views.searchResult),
    url(r'^playlists$', views.playlists),
    url(r'^(?P<id>\d+)$', views.addSongYourMusic)
]