import uuid
from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=50, blank=False)

    class Meta:
        verbose_name = 'application'

    def __str__(self):
        return self.name
