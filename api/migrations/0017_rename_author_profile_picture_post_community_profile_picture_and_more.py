# Generated by Django 5.1.2 on 2024-11-28 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_post_author_profile_picture_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author_profile_picture',
            new_name='community_profile_picture',
        ),
        migrations.AddField(
            model_name='comment',
            name='author_profile_picture',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
