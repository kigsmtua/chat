"""Lets define what a message looks like."""
from random import randint
from chat.models import Messages, Thread
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class MessageCreateSerializer(ModelSerializer):
    """Define all values required to create a message."""

    class Meta:
        """Required properties for a message."""

        sender = SerializerMethodField()
        model = Messages
        fields = [
            'text',
            'receiver',
            'sender'
        ]

    # @TODO add support for group chat
    def create(self, validated_data):
        """
        Given a dictionary of deserialized field values, either update.

        an existing model instance, or create a new model instance.
        """
        receiver = validated_data['receiver']
        sender = self.request.user
        thread_name = receiver.username + sender.username
        try:
            thread = Thread.objects.get(name=thread_name)
        except Exception:
            thread = Thread.objects.create(name=thread_name)
        message = Messages.objects.create(author=sender, thread=thread **validated_data) # noqa
        return message

    def get_sender(self, obj):
        """Get sender from request."""
        try:
            sender = obj.user
        except:
            sender = None
        return sender
