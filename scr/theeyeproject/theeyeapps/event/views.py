from .models import Event
from application.models import Application
from .serializer import *
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows event to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('-timestamp')
    serializer_class = EventSerializer
    permission_classes = [permissions.BasePermission]

    def create(self, request):
        """
        Save a Event message
        :param request:
            {
                "session_id": "",
                "name": "",
                "category": "",
                "data": ""
            }
        :return: Status 200 Event created, Status 400 Not valid request
        """
        if request.method == 'POST':
            header_application = request.META.get("HTTP_APPLICATIONID")
            if header_application is not None:
                try:
                    application = Application.objects.get(id=header_application)
                except Exception:
                    return Response({"status": "error", "application_id": "Not a valid application id"},
                                    status=status.HTTP_400_BAD_REQUEST)

                event_serializer = EventSerializer(data=request.data, context=application.id)
                if event_serializer.is_valid():
                    event_serializer.save()
                    return Response({"status": "success"}, status=status.HTTP_201_CREATED)
                else:
                    return Response({"status": "error", "data": event_serializer.errors},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"status": "error", "application_id": "Not a valid application id"},
                                status=status.HTTP_400_BAD_REQUEST)

