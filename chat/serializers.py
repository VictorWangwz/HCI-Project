__author__ = ' Zhen Wang'

from rest_framework.serializers import ModelSerializer
from .model import *


class VideoSerialzier(ModelSerializer):

    class Meta:
        model = Video
        fields = "__all__"



class ChatRoomSerialzier(ModelSerializer):

    class Meta:
        model = ChatRoom
        fields = "__all__"