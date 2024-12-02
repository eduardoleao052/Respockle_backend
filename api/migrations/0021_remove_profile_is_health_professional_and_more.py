# Generated by Django 5.1.2 on 2024-11-30 00:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_post_warning'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_health_professional',
        ),
        migrations.AddField(
            model_name='post',
            name='warn_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts_warned', to=settings.AUTH_USER_MODEL),
        ),
    ]