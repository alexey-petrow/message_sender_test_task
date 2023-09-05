from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'username', 'first_name', 'token', 'date_joined']


admin.site.register(CustomUser, CustomUserAdmin)
