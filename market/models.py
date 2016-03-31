from django.db import models
from django.utils import timezone


class Service(models.Model):
    service_provider = models.ForeignKey('auth.User')
    client_username = models.CharField(max_length=50, default="username")
    title = models.CharField(max_length=100, default="Service")
    description = models.TextField()
    location = models.CharField(max_length=50, default="U.S.")
    final_time = models.CharField(max_length=20, default="0")
    category = models.CharField(max_length=50, default="Other")
    bid = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
