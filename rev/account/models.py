from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    first_name=models.CharField(max_length=15)
    email=models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def __str__(self):
        return f"{self.email} ({self.first_name})"