from django.db import models
from django.conf import settings
from cities_light.models import Country

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    activity = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    building_no = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    email = models.EmailField()
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name