# Generated by Django 5.0.6 on 2024-05-30 03:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("educations", "0006_alter_education_end_date_alter_education_start_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="education",
            name="end_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="education",
            name="start_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]