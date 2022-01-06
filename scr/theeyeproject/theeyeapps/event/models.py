from django.db import models
from jsonfield import JSONField


class Event(models.Model):
    session_id = models.CharField(max_length=70, blank=False, default=None)
    category = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=100, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, blank=False)
    data = JSONField(blank=False, default="")

    class Meta:
        verbose_name = 'event'

    def __str__(self):
        return self.name
