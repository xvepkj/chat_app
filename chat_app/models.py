from django.db import models

# chat_app/models.py

class ChatRoom(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

