# Generated by Django 4.2.7 on 2023-12-12 05:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0009_register_event"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventpoints",
            name="event_points",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
