"""Lets define what a message looks like."""
# This means all application values come back up and pass the maintainance

from rest_framework.serializers import ModelSerializer
from chat.models import Messages, Thread


class MessageCreateSerializer(ModelSerializer):
    """Define all values required to create a message"""

    # Message belongs to a message
    # This means that we can have a thread group as well
    class Meta:
        """Define message attributess."""
        model = Messages
        fields = [
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'profile'
        ]

    def create(self, validated_data):
        """
        Given a dictionary of deserialized field values, either update.

        an existing model instance, or create a new model instance.
        """
        profile_data = validated_data.pop('profile')
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name) # noqa
        Profile.objects.create(user=user, **profile_data)
        return user
