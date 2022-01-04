from .models import Event
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows event to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('-timestamp')
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
