# Generated by Django 5.1.5 on 2025-02-09 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileImg',
            field=models.ImageField(default='profile_images/blank-profile-picture.png', upload_to='profile_images'),
        ),
    ]
