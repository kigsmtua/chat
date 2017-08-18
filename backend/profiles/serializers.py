"""Serializers for the profile module."""
from django.contrib.auth.models import User

from profiles.models import Profile
from rest_framework.serializers import ModelSerializer


class ProfileSerializer(ModelSerializer):
    """Profile details."""
    class Meta:
        model = Profile
        fields = [
          'profile_pic'
        ]

    def get_profile_pic(self, obj):
        """Absolute url to the profile pic."""
        try:
            profile_pic = obj.upload.url
        except:
            profile_pic = None
        return profile_pic


# @TODO implement validation
class ProfileCreateSerializer(ModelSerializer):
    """Define all values required to create a profile."""

    profile = ProfileSerializer()

    class Meta:
        """Define profile attributess."""

        model = User
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
