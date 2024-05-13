from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    role_choice = (
        ('user', 'user'),
        ('company', 'company'),
    )
    
    role = models.CharField(max_length=20, choices=role_choice)
    
    