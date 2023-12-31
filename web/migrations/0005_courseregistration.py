# Generated by Django 4.2.7 on 2023-11-25 05:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0004_rename_duaration_course_duration"),
    ]

    operations = [
        migrations.CreateModel(
            name="CourseRegistration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.IntegerField()),
                ("message", models.TextField()),
            ],
        ),
    ]
