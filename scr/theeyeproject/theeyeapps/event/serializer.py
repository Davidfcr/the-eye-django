from .models import Event
from rest_framework import serializers
from django.contrib.auth import SESSION_KEY
from django.contrib.sessions.models import Session
from .schemas import *


class EventSerializer(serializers.ModelSerializer):
    data = serializers.JSONField()

    class Meta:
        model = Event
        fields = ['id', 'session_id', 'name', 'category', 'timestamp', 'data']

    def validate_session_id(self, value):
        try:
            session = Session.objects.get(session_key=value)
            session.get_decoded()[SESSION_KEY]
            return value
        except Exception:
            raise serializers.ValidationError({"session_id": "Invalid session id"})


    def validate(self, data):
        name = data["name"].replace(" ", "")
        category = data["category"].replace(" ", "")
        application_id = self.context
        payload_schema_name = "{0}_{1}_{2}".format(category, name, application_id).capitalize()
        try:
            payload_schema = globals()[payload_schema_name]
            payload_schema.validate(data["data"])
            return data
        except Exception:
            raise serializers.ValidationError({"data": "Not valid data payload"})

