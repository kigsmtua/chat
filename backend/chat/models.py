"""Chat models."""
from django.db import models

from profiles.models import Profile


class Thread(models.Model):
    """A collection of messages defined in a thread."""

    name = models.TextField()
    createdAt = models.DateTimeField(auto_now=False, auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True, auto_now_add=False)


class Messages(models.Model):
    """Defines a single chat message."""

    author = models.ForeignKey(Profile, related_name="sender")
    receiver = models.ForeignKey(Profile, related_name="receiver")
    text = models.TextField()
    isRead = models.BooleanField(default=0)
    thread = models.ForeignKey(Thread, related_name="thread")
    sentAt = models.DateTimeField(auto_now=False, auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True, auto_now_add=False)
