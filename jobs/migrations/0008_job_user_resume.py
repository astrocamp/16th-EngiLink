# Generated by Django 5.0.6 on 2024-05-23 10:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0007_remove_job_resume_user_job_user"),
        ("resumes", "0003_resume_posit"),
    ]

    operations = [
        migrations.AddField(
            model_name="job_user",
            name="resume",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="resumes.resume",
            ),
        ),
    ]
