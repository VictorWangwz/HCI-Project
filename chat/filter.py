__author__ = ' Zhen Wang'

import django_filters
from .model import Video


class VideoFilter(django_filters.FilterSet):

    class Meta:
        model = Video
        fields = ['key', 'category']