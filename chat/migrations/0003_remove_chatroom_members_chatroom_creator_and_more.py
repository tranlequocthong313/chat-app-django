# Generated by Django 4.1.5 on 2023-01-11 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_remove_chatroom_creator_chatroom_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='members',
        ),
        migrations.AddField(
            model_name='chatroom',
            name='creator',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='chat_rooms', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='chat_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chat.chatroom'),
        ),
    ]