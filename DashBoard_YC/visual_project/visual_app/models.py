from django.db import models
from django.db import connection
# Create your models here.
import datetime
from django.utils import timezone


class User(models.Model):
    username=models.CharField(max_length=16)
    password=models.CharField(max_length=32)

    def __str__(self):
        return self.username