# Generated by Django 5.0.4 on 2024-05-12 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('educations', '0001_initial'),
        ('resume', '0004_delete_work'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Educations',
            new_name='Education',
        ),
    ]
