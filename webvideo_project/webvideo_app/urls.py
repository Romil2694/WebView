from django.urls import path
from . import views

urlpatterns = [
    path('video_stream/', views.webvideo, name='video_stream')
]