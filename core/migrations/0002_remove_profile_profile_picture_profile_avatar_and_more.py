# Generated by Django 5.2 on 2025-05-17 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
