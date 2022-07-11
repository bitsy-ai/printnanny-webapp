from django.contrib import admin
from print_nanny_webapp.devices.models import Device, JanusStream


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("hostname", "user", "created_dt")
    model = Device


@admin.register(JanusStream)
class JanusStreamAdmin(admin.ModelAdmin):
    list_display = (
        "device",
        "device_hostname",
        "active",
        "config_type",
        "created_dt",
    )
    model = JanusStream

    @admin.display(ordering="device__hostname", description="Device Hostname")
    def device_hostname(self, obj):
        return obj.device.hostname
