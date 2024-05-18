# Generated by Django 5.0.6 on 2024-05-18 13:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_initial'),
        ('jobs', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='companies.company'),
            preserve_default=False,
        ),
    ]
