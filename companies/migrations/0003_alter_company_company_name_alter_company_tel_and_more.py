# Generated by Django 5.0.6 on 2024-05-20 07:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("companies", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="company_name",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="company",
            name="tel",
            field=models.CharField(default="", max_length=11),
        ),
        migrations.AlterField(
            model_name="company",
            name="tin",
            field=models.CharField(default="", max_length=8),
        ),
        migrations.AlterField(
            model_name="company",
            name="user_name",
            field=models.CharField(default="", max_length=100),
        ),
    ]
