# Generated by Django 5.0.4 on 2024-05-04 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]
