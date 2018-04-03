from django.conf.urls import *
from . import views

urlpatterns = [# album urls
               url(r'^album/', views.album),
               # music_type urls
               url(r'^music_type/', views.music_type),
               # music_type urls
               url(r'^music_sub_type/', views.music_sub_type),
               # album-music_type relationship urls
               url(r'^album_music_type/', views.album_music_type),
               # music_type-music_sub_type relationship urls
               url(r'^music_type_music_sub_type/', views.music_type_music_sub_type),
            ]