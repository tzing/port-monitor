from django.contrib import admin

from . import models


@admin.register(models.MonitorTarget)
class BasicAdmin(admin.ModelAdmin):
    ...
