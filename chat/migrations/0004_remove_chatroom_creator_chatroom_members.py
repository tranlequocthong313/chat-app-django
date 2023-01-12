# Generated by Django 4.1.5 on 2023-01-11 12:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0003_remove_chatroom_members_chatroom_creator_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='creator',
        ),
        migrations.AddField(
            model_name='chatroom',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
