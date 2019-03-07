__author__ = ' Zhen Wang'

from django.contrib import admin
from .model import *

admin.site.register(User)
admin.site.register(Video)