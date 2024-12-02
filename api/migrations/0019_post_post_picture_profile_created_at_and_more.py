# Generated by Django 5.1.2 on 2024-11-29 20:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_community_community_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_picture',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='community',
            name='community_picture',
            field=models.ImageField(blank=True, default='../assets/default_community_image.png', null=True, upload_to='community_pictures/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default=''),
        ),
    ]
