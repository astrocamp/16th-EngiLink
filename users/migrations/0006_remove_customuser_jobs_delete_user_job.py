# Generated by Django 5.0.6 on 2024-05-20 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_user_job_customuser_jobs"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="jobs",
        ),
        migrations.DeleteModel(
            name="User_Job",
        ),
    ]
