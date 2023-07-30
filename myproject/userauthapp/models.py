from django.db import models
from datetime import datetime

# Create your models here.
class Signup(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default="")
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    date = models.DateTimeField(default=datetime.today)

    def __str__(self):
        return self.username