"""Lets define what a message looks like."""

from chat.models import Messages, Thread
from rest_framework.serializers import ModelSerializer


# @TODO improve this implementation
class ThreadCreateSerializer(ModelSerializer):
    """Define all values required to create a message."""

    class Meta:
        """Define message attributess."""

        model = Thread
        fields = [
            'text'
        ]

    def create(self, validated_data):
        """
        Given a dictionary of deserialized field values, either update.

        an existing model instance, or create a new model instance.
        """
        thread = Thread.objects.create(**validated_data)
        message = Messages.objects.create(author=self.request.user, thread=thread **validated_data) # noqa
        return message
