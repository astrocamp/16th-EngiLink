# Generated by Django 5.0.6 on 2024-05-20 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("works", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="work",
            name="posit",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
