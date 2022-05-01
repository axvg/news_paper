from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    occupation = models.CharField(max_length=63, blank=True, null=True)