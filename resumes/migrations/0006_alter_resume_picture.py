# Generated by Django 5.0.6 on 2024-05-24 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0005_alter_resume_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='picture',
            field=models.FileField(null=True, upload_to='img/'),
        ),
    ]
