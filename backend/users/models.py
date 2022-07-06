from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    username = models.CharField(max_length=500, unique=True, null=True)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
   
    REQUIRED_FIELDS = []
