# Generated by Django 5.0.6 on 2024-05-17 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('tin', models.CharField(max_length=8)),
                ('user_name', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=11)),
            ],
        ),
    ]
