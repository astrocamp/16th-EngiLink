# Generated by Django 5.0.6 on 2024-05-20 09:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0005_alter_job_company"),
        ("users", "0004_alter_customuser_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="User_Job",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("collect", models.BooleanField(default=False)),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="jobs.job"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "job")},
            },
        ),
        migrations.AddField(
            model_name="customuser",
            name="jobs",
            field=models.ManyToManyField(through="users.User_Job", to="jobs.job"),
        ),
    ]