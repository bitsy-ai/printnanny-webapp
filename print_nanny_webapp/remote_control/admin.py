from django.contrib import admin
from django.apps import apps
# Register your models here.

OctoPrintDevice = apps.get_model("remote_control", "OctoPrintDevice")
@admin.register(OctoPrintDevice)

class OctoPrintDeviceAdmin(admin.ModelAdmin):

    list_display = ("id", "user", "serial", "cloudiot_device_id")
    list_filters = ("id", "user", "serial", "cloudiot_device_id")
    