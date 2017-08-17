"""Profile associated views."""
from django.conf.urls import url

from profiles.views import ProfileCreateAPI

urlpatterns = [
    url(r'^create/', ProfileCreateAPI.as_view(), name="register"),
]
