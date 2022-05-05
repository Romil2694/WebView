from django.shortcuts import render, redirect
from django.http import StreamingHttpResponse
from .camera import videocapture


# Create your views here.

def index(request):
    return render(request, './index.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_stream(request):
    return StreamingHttpResponse(gen(videocapture()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')
