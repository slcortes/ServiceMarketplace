from django.contrib import admin
from .models import Service, Review, Bid


admin.site.register(Service)
admin.site.register(Bid)
admin.site.register(Review)
