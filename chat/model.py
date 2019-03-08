__author__ = ' Zhen Wang'

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)


class Video(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to="videos/", null=True, blank=True)


class ChatRoom(models.Model):
    name = models.CharField(max_length=50)
