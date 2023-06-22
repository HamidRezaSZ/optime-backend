from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import *


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    list_display = ("id", "username", "email", "first_name", "last_name", "is_staff")
