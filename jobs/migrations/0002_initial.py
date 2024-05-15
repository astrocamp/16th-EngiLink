# Generated by Django 5.0.6 on 2024-05-15 13:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("jobs", "0001_initial"),
        ("resumes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="job_resume",
            name="resume",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="resumes.resume"
            ),
        ),
        migrations.AddField(
            model_name="job",
            name="resumes",
            field=models.ManyToManyField(
                through="jobs.Job_Resume", to="resumes.resume"
            ),
        ),
    ]
