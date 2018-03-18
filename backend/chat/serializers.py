"""Lets define what a message looks like."""
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from chat.models import Messages, Thread
from profiles.models import Profile


class MessageCreateSerializer(ModelSerializer):
    """Define all values required to create a message."""

    class Meta:
        """Required properties for a message."""

        sender = SerializerMethodField()
        model = Messages
        fields = [
            'text',
            'receiver',
        ]

    # @TODO add support for group chat
    def create(self, validated_data):
        """
        Given a dictionary of deserialized field values, either update.

        an existing model instance, or create a new model instance.
        """
        receiver = validated_data['receiver']
        message = validated_data['text']
        logged_in_user = self.context['request'].user
        sender = Profile.objects.get(user=logged_in_user)
        thread_name = receiver.user.username + logged_in_user.username
        try:
            thread = Thread.objects.get(name=thread_name)
        except BaseException as e:
            thread = Thread.objects.create(name=thread_name)
        message = Messages.objects.create(sender=sender, receiver=receiver, thread=thread, text=message) # noqa
        return message
