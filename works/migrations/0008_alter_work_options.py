# Generated by Django 5.0.6 on 2024-06-08 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0007_alter_work_is_current'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='work',
            options={'ordering': ['posit']},
        ),
    ]
