"""Chat application views."""
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from chat.models import Messages
from chat.serializers import MessageCreateSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny


class MessageCreateView(CreateAPIView):
    """Create a message here."""

    serializer_class = MessageCreateSerializer
    queryset = Messages.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_context(self):
        """Pass request object to serializer."""
        return {'request': self.request}


@login_required
def index(request):
    """
    Root page view.

    This is essentially a single-page app, if you ignore the
    login and admin parts.
    """
    rooms = {}
    return render(request, "index.html", {
        "rooms": rooms,
    })

def health_check(request):
    return HttpResponse("Ok()..", content_type="application/json")
