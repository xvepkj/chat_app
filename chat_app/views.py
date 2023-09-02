# chat_app/views.py

from django.shortcuts import render
from .models import ChatRoom

def chat_room(request, room_name):
    return render(request, 'chat_app/chat_room.html', {
        'room_name': room_name
    })

def chat_room_list(request):
    chat_rooms = ChatRoom.objects.all()
    return render(request, 'chat_app/chat_room_list.html', {'chat_rooms': chat_rooms})


