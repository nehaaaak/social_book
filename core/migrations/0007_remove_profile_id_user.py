# Generated by Django 5.1.5 on 2025-02-11 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_profile_id_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id_user',
        ),
    ]
