# chat/urls.py
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

from . import views

urlpatterns = [
    path('chat/', views.index, name='index'),
    path('<str:user_name>/chat/<str:room_name>/', views.room, name='room'),
    path('users/', UserList.as_view()),
    path('videos/', VideoList.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)