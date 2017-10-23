"""Chat models."""
import json

from django.db import models

from profiles.models import Profile


class Thread(models.Model):
    """A collection of messages defined in a thread."""

    name = models.CharField(max_length=255, unique=True)
    createdAt = models.DateTimeField(auto_now=False, auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    def send_message(self, message, user):
        """Called to send a message to a user."""
        msg = {
            'thread_id': str(self.id),
            'thread_name': str(self.id),
            'message': message}

        self.name.send(
            {"message": json.dumps(msg)}
        )


class Messages(models.Model):
    """Defines a single chat message."""

    sender = models.ForeignKey(Profile, related_name="sender")
    receiver = models.ForeignKey(Profile, related_name="receiver")
    text = models.TextField()
    isRead = models.BooleanField(default=0)
    thread = models.ForeignKey(Thread, related_name="thread")
    sentAt = models.DateTimeField(auto_now=False, auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True, auto_now_add=False)
