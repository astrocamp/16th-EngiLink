# Generated by Django 5.0.4 on 2024-05-12 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_delete_education'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Work',
        ),
    ]