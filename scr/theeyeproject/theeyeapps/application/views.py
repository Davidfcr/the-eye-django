from .models import Application
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import ApplicationSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows applications to be viewed or edited.
    """
    queryset = Application.objects.all().order_by('-name')
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
