from django.contrib import admin

from .models import *


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'driver', 'description', 'done')
    list_editable = ('done',)
    list_filter = ('done', 'driver')
