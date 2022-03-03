import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class ProxyLists(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    ip_address = models.GenericIPAddressField(null=True)
    port = models.IntegerField(null=True, blank=True)
    protocol = models.CharField(max_length=15, null=True, blank=True)
    anonymity = models.CharField(max_length=30, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    region = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    uptime = models.CharField(max_length=15, null=True, blank=True)
    response = models.CharField(max_length=15, null=True, blank=True)
    speed = models.CharField(max_length=15, null=True, blank=True)
    last_checked = models.CharField(max_length=30, blank=True)
