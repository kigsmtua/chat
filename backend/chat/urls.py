"""Chat associated views."""
from django.conf.urls import url

from chat.views import MessageCreateView

urlpatterns = [
    url(r'^create/', MessageCreateView.as_view(), name="register"),
]
