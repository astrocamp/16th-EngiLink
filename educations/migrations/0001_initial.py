# Generated by Django 5.0.6 on 2024-05-15 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Education",
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
                ("school_name", models.CharField(max_length=100)),
                ("major", models.CharField(max_length=100)),
                (
                    "degree",
                    models.CharField(
                        choices=[
                            ("1", "高中職以下"),
                            ("2", "高中職"),
                            ("3", "專科"),
                            ("4", "學士"),
                            ("5", "碩士"),
                            ("6", "博士"),
                            ("7", "肄業"),
                        ],
                        max_length=1,
                    ),
                ),
                ("start_date", models.DateField(blank=True, null=True)),
                ("end_date", models.DateField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
