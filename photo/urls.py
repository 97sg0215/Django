from django.conf.urls import url
from photo.views import *

app_name = 'photo'
urlpatterns = [
    url(r'^$', AlbumLV.as_view(model=Album), name='index'),

    url(r'^album/$', ListView.as_view(model=Album), name='album_list'),

    url(r'^album/(?P<pk>\d+)/$', DetailView.as_view(model=Album), name='album_detail'),

    url(r'^photo/(?P<pk>\d+)/$', DetailView.as_view(model=Photo), name='photo_detail'),
]