# Generated by Django 2.1.5 on 2019-02-18 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messages', '0003_auto_20190218_1353'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-sent_at']},
        ),
    ]