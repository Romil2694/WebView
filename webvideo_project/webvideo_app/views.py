from django.shortcuts import render, redirect
from django.http import StreamingHttpResponse
from .camera import videocapture


# Create your views here

def webvideo(request):
    return render(request, './webvideo.html')
