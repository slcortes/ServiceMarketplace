from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings


class Service(models.Model):
    client= models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='service_client',
        null=True,
        blank=True
    )
    service_provider = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='service_service_providers',
        null=True,
        blank=True
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=50, default="U.S.")
    final_time = models.CharField(max_length=20, default="0")
    category = models.CharField(max_length=50, default="Other")
    bid = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=1000.00
    )
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


        
"""        
class User(settings.User ??):  # how to add to current User model?
    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return mean(all_ratings)
"""
    
    
    
class Review(models.Model):
    RATINGS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    rating = models.IntegerField(choices=RATINGS)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='review')
    author = models.CharField(max_length=200, default="your name")
    comment = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment