from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from web_project import settings

class CustomUser(AbstractUser):
    # Any extra fields would go here
    def __str__(self):
        return self.email

class Message(models.Model):
    content = models.CharField(max_length=360);
    created_date = models.DateTimeField(default=timezone.now)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    to_user = models.CharField(max_length=360)
