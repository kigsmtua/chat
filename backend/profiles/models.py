from django.db import models
from django.contrib.auth.models import User


def upload_location(instance, filename):
    new_id = randint(0, 1000)
    return "%s/%s" % (new_id, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,    related_name="profile")
    unique_name = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    what_makes_you_happy = models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField(
        upload_to=upload_location,
        null=True,
        blank=True,
        width_field="width_field",
        height_field="height_field")
    height_field = models.IntegerField(default=0, blank=True)
    width_field = models.IntegerField(default=0, blank=True)
