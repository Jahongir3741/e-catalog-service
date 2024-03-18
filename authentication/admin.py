from django.contrib import admin
from .models import User, Admin, Employee, LowUser
from django.contrib.auth.models import Permission, ContentType


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(User)
class UserAdmins(admin.ModelAdmin):
    fields = ['username','role', 'password', 'is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions',]
    # exclude = ['email', 'first_name', 'last_name']
    list_display = ["username", 'is_staff']
    search_fields = ['username']
    # filter_horizontal = ['user_permissions', 'groups']
    filter_vertical = ['user_permissions']
    autocomplete_fields = ['groups']


admin.site.register([Employee, Admin, LowUser, ContentType])
