from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Business(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='business')
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='business_logo/', blank=False)

    def __str__(self):
        return self.name
# Create your models here.
