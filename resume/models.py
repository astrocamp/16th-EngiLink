from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    account = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user_id}: {self.account}"

class ProfileManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at=None)

class Profile(models.Model):
    GENDER_CHOICES = [
        ('M', '男'),
        ('F', '女'),
        ('N', '不透露'),
    ]
    EXPERIENCE_CHOICES = [
        ('1年以下', '一年以下'),
        ('3年以下', '三年以下'),
        ('3年以上', '三年以上'),
        ('5年以上', '五年以上'),
    ]
    SKILL_CHOICES = [
        ('Python', 'Python'),
        ('JavaScript', 'JavaScript'),
        ('Java', 'Java'),
        ('C++', 'C++'),
        ('HTML/CSS', 'HTML/CSS'),
        ('PHP', 'PHP'),
        ('Ruby', 'Ruby'),
        ('Swift', 'Swift'),
        ('其他', '其他'),
    ]
    DEGREE_CHOICES = [
        ('1', '高中職以下'),
        ('2', '高中職'),
        ('3', '專科'),
        ('4', '學士'),
        ('5', '碩士'),
        ('6', '博士'),
        ('7', '肄業'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField(null=True, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True) 
    skills = models.CharField(max_length=200, null=True, blank=True)

    # education
    school_name = models.CharField(max_length=100, default='')
    major = models.CharField(max_length=100, default='')
    degree = models.CharField(max_length=1, choices=DEGREE_CHOICES, default='')
    education_start_date = models.DateField(null=True, blank=True)
    education_end_date = models.DateField(null=True, blank=True)

    # work
    company_name = models.CharField(max_length=100, default='')
    position = models.CharField(max_length=100, default='')
    work_start_date = models.DateField(null=True, blank=True)
    work_end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)

    # project
    project_name = models.CharField(max_length=100, default='')
    responsibility = models.CharField(max_length=200, default='')
    technologies_used = models.CharField(max_length=200, default='')
    description = models.TextField(null=True, blank=True)

    # sort delete
    deleted_at = models.DateTimeField(null=True)
    objects = ProfileManager() 

    def __str__(self):
        return f"{self.name}'s Profile ({self.profile_id})"

    def delete(self):
        self.deleted_at = timezone.now()  
        self.save()
    
    def get_skills(self):
        return self.skills.split(', ')



