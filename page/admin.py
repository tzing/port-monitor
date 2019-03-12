from django.contrib import admin

from . import models


@admin.register(models.MonitorTarget, models.Setting)
class BasicAdmin(admin.ModelAdmin):
    ...
