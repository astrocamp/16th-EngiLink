from django.db import models
from resumes.models import Resume

class Project(models.Model):
    SKILL_CHOICES = [(skill, skill) for skill in ['Python', 'JavaScript', 'Java', 'C++', 'HTML/CSS', 'PHP', 'Ruby', 'Swift', '其他']]

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    responsibility = models.CharField(max_length=200)
    technologies_used = models.CharField(max_length=200,null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null = True)


    objects = models.Manager() 

    def __str__(self):
        return f"{self.name}'s Resume ({self.resume_id})"
    
    def get_technologies(self):
        return self.technologies_used.split(', ')
