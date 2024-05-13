from django.db import models
from resume.models import Profile
from django.utils import timezone


class Work(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = models.Manager()  
    def __str__(self):
        return f"{self.name}'s Profile ({self.profile_id})"

    def soft_delete(self):
        self.deleted_at = timezone.now() 
        self.save()