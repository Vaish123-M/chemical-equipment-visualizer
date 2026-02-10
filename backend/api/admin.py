from django.contrib import admin

from .models import EquipmentDataset


@admin.register(EquipmentDataset)
class EquipmentDatasetAdmin(admin.ModelAdmin):
    list_display = ("id", "upload_time", "total_count")
    ordering = ("-upload_time",)
