"""Chat application views."""
from chat.models import Messages
from chat.serializers import ThreadCreateSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny


class MessageCreateView(CreateAPIView):
    """Create a message here."""

    serializer_class = ThreadCreateSerializer
    queryset = Messages.objects.all()
    permission_classes = [AllowAny]
