"""User definitions."""
from random import randint

from django.contrib.auth.models import User
from django.db import models


# @TODO move to an s3 bucket
def upload_location(instance, filename):
    """Specify where files in our default root are uploaded."""
    new_id = randint(0, 1000)
    return "%s/%s" % (new_id, filename)


class Profile(models.Model):
    """Describe a user in our system."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile") # noqa
    profile_pic = models.ImageField(
        upload_to=upload_location,
        null=True,
        blank=True,
        width_field="width_field",
        height_field="height_field")
    height_field = models.IntegerField(default=0, blank=True)
    width_field = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.user.username
