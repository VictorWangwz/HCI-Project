# chat/views.py
import json

from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils.safestring import mark_safe
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import *
from rest_framework.views import APIView

from .model import *
from .serializers import VideoSerialzier


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, user_name, room_name):
    video = get_object_or_404(Video, name=room_name)
    user = get_object_or_404(User, name=user_name)
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'video': video,
        'user': mark_safe(json.dumps(user.name))
    })


class UserList(APIView):

    def get(self, request):
        return Response([user.name for user in User.objects.all()])

    def post(self, request):
        user = User.objects.create(**request.data)
        return Response({
            "name": user.name,
            "id":user.id
        })


class VideoList(ListCreateAPIView):
    serializer_class = VideoSerialzier

    def get_queryset(self):
        return Video.objects.all()
