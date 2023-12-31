# Generated by Django 4.1.5 on 2023-08-27 17:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kinect", "0002_newpost_following"),
    ]

    operations = [
        migrations.RemoveField(model_name="newpost", name="following",),
        migrations.AddField(
            model_name="user",
            name="follower",
            field=models.ManyToManyField(
                related_name="user_followers", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="following",
            field=models.ManyToManyField(
                related_name="user_following", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
