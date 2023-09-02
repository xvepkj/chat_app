# chat_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
    path('rooms/', views.chat_room_list, name='chat_room_list'),  # List chat rooms
]
