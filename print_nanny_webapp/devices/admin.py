from django.contrib import admin
from print_nanny_webapp.devices.models import Device, WebrtcStream


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("hostname", "user", "created_dt")
    model = Device


@admin.register(WebrtcStream)
class WebrtcStreamAdmin(admin.ModelAdmin):
    list_display = (
        "device",
        "device_hostname",
        "active",
        "config_type",
        "created_dt",
    )
    model = WebrtcStream

    @admin.display(ordering="device__hostname", description="Device Hostname")
    def device_hostname(self, obj):
        return obj.device.hostname
