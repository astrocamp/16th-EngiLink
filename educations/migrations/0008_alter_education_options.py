# Generated by Django 5.0.6 on 2024-06-08 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('educations', '0007_alter_education_end_date_alter_education_start_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ['posit']},
        ),
    ]
