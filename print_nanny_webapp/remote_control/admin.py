from django.contrib import admin
from django.apps import apps

# Register your models here.

OctoPrintDevice = apps.get_model("remote_control", "OctoPrintDevice")


@admin.register(OctoPrintDevice)
class OctoPrintDeviceAdmin(admin.ModelAdmin):

    list_display = ("id", "user", "serial", "name", "cloudiot_device_num_id")
    list_filters = ("id", "user", "serial", "name", "cloudiot_device_num_id")
