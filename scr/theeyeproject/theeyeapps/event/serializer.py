from .models import Event
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'session_id', 'name', 'category', 'timestamp', 'data']

    def validate_data(self, value):
        return value

    def validate_session_id(self, value):
        session = self.context.session.session_key
        if session is not value:
            raise serializers.ValidationError("Invalid session id")
        return value


class ApplicationPageInteractionPageView(serializers.Serializer):
    host = serializers.CharField(required=True, max_length=100)
    path = serializers.CharField(required=True, max_length=100)
