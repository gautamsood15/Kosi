# Generated by Django 4.1 on 2022-08-20 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("AtbaraApp", "0004_video_views"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="video",
            name="Views",
        ),
    ]
