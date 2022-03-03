from django.contrib.auth.models import AbstractUser, UserManager
import uuid
from django.db import models
# Create your models here.

class UsuarioManager(UserManager):

    def _create_user(self, username, password, **extra_fields):
        print(dir(self))
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, password, **extra_fields)
        
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


class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', blank=True, null=True)
    username = models.CharField("Usuario", max_length=30, unique=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    objects = UsuarioManager()