from django.contrib.auth.models import AbstractUser
from django.db import models

class CompanyUser(AbstractUser):
    email = models.EmailField(max_length=255)
    company_name = models.CharField(max_length=100)
    tin = models.CharField(max_length=8)
    user_name = models.CharField(max_length=100)
    tel = models.CharField(max_length=10)

    