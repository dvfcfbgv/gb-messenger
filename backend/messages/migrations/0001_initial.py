# Generated by Django 2.1.5 on 2019-02-17 05:40

import backend.utils
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chatrooms', '0001_initial'),
        ('chatroom_memberships', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('unique_identifier', models.CharField(default=backend.utils.id_generator, max_length=8, primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=1000)),
                ('sent_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('edited_at', models.DateTimeField(auto_now_add=True)),
                ('chatroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chatrooms.Chatroom')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to='chatroom_memberships.ChatroomMembership')),
            ],
            options={
                'ordering': ['sent_at'],
            },
        ),
    ]
