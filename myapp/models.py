from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from PIL import Image

import os

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    read_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Message(models.Model):
    from_email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    subject = models.CharField(max_length=50, null=True, blank=True)
    message = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.message[:20]