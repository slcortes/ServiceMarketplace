from django.db import models
from django.utils import timezone


class Service(models.Model):
    service_provider = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100, default="Service")
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        self.title
