from django.contrib import admin
from .models import Post, Community, Comment, Profile, User, CustomUserAdmin


# Register your models here.
admin.site.register(Post)
admin.site.register(Community)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
