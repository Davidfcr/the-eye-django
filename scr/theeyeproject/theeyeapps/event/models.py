from django.db import models


class Event(models.Model):
    category = models.CharField(max_length=50, blank=False)
    name = models.CharField(max_length=50, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    data = models.TextField()

    def __str__(self):
        return self.name
