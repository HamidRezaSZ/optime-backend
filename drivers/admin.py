from django.contrib import admin

from .models import *


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'longitude', 'latitude', 'free')
    list_editable = ('free',)
    list_filter = ('free', 'user')
