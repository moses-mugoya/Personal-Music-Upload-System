from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<song>[-\w]+)/$', views.song_detail, name='song_detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<song>[-\w]+)/$', views.song_lyrics, name='song_lyrics'),
    url(r'^breaking_free_lyrics/(?P<song_id>[0-9]+)$', views.breaking_free, name='breaking_free'),
    url(r'^god_like_you_lyrics/(?P<song_id>[0-9]+)$', views.god_like, name='god_like')
]
