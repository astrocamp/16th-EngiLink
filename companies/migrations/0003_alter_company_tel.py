# Generated by Django 5.0.6 on 2024-05-15 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_remove_company_email_company_custom_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='tel',
            field=models.CharField(max_length=11),
        ),
    ]