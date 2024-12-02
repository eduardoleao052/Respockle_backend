from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

User.add_to_class('is_health_professional', models.BooleanField(default=False))

# Customize the admin to include the new field


# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='communities_created_by_user', default=1)
    author_username = models.TextField(default='')
    members = models.ManyToManyField(User, related_name="communities")
    community_picture = models.ImageField(default='../assets/default_community_image.png', upload_to='community_pictures/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_picture = models.ImageField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    author_username = models.TextField(default='')
    author_is_health_professional = models.BooleanField(default=False)
    community_profile_picture = models.ImageField(default='')
    likes = models.IntegerField(default=0)
    liked_by_user = models.ManyToManyField(User, related_name="liked_posts")
    reports = models.IntegerField(default=0)
    reported_by_user = models.ManyToManyField(User, related_name="reported_posts")
    community = models.ForeignKey(Community, related_name="posts_in_community", on_delete=models.CASCADE)
    saved_by_user = models.ManyToManyField(User, related_name="saved_posts")
    warning = models.TextField(default='')
    warn_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts_warned', null=True, blank=True)
    warn_author_username = models.TextField(default='')


    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    author_username = models.TextField(default='')
    author_profile_picture = models.ImageField(default='')
    author_is_health_professional = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    liked_by_user = models.ManyToManyField(User, related_name="liked_comments")
    post = models.ForeignKey(Post, related_name="comments_in_post", on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title + ' comment'
    
class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=100, default='')
    bio = models.TextField(default='')
    profile_picture = models.ImageField(default='../assets/default_profile_picture.png')

    def __str__(self):
        return self.email