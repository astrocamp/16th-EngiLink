from django.db import models
from resumes.models import Resume
from django.utils import timezone
from positions.fields import PositionField

class Work(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,related_name='works')
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    posit = PositionField(collection='resume')
    objects = models.Manager()

    def __str__(self):
        return f"{self.name}'s Resume ({self.resume_id})"

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()
