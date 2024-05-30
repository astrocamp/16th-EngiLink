# Generated by Django 5.0.6 on 2024-05-30 06:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_alter_job_resume_accepted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='address',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='job',
            name='experience',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]