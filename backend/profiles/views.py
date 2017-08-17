"""Profile creation views."""
from profiles.models import Profile
from profiles.serializers import ProfileCreateSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny


class ProfileCreateAPI(CreateAPIView):
    """Profile create view."""

    serializer_class = ProfileCreateSerializer
    queryset = Profile.objects.all()
    permission_classes = [AllowAny]
