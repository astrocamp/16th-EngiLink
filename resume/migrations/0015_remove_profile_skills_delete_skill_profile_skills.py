# Generated by Django 5.0.4 on 2024-05-03 15:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resume", "0014_skill_profile_skills"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="skills",
        ),
        migrations.DeleteModel(
            name="Skill",
        ),
        migrations.AddField(
            model_name="profile",
            name="skills",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Python", "Python"),
                    ("JavaScript", "JavaScript"),
                    ("Java", "Java"),
                    ("C++", "C++"),
                    ("HTML/CSS", "HTML/CSS"),
                    ("PHP", "PHP"),
                    ("Ruby", "Ruby"),
                    ("Swift", "Swift"),
                    ("其他", "其他"),
                ],
                max_length=200,
                null=True,
            ),
        ),
    ]
