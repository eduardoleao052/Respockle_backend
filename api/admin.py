from django.contrib import admin
from .models import Post, Community, Comment, Profile, User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('is_health_professional',)
    fieldsets = UserAdmin.fieldsets + (
        (_('Additional Info'), {'fields': ('is_health_professional',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (_('Additional Info'), {'fields': ('is_health_professional',)}),
    )
# Register your models here.
admin.site.register(Post)
admin.site.register(Community)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
