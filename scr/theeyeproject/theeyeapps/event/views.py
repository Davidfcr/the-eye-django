from .models import Event
from .serializer import *
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows event to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('-timestamp')
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

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
            application = request.META.get("HTTP_APPLICATION_ID", "")

            request.data['data'] = json.dumps(request.data['data'])
            event_serializer = EventSerializer(data=request.data, context=request)
            if event_serializer.is_valid():
                if event_serializer.data["session_id"] is not request.session.session_key:
                    return JsonResponse(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                return JsonResponse(event_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
