from django.contrib import admin
from print_nanny_webapp.devices.models import Device, JanusStream, JanusAuth


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
        "info",
        "config_type",
        "created_dt",
    )
    model = JanusStream

    @admin.display(ordering="device__hostname", description="Device Hostname")
    def device_hostname(self, obj):
        return obj.device.hostname


@admin.register(JanusAuth)
class JanusAuthAdmin(admin.ModelAdmin):
    list_display = ("user", "user_email", "config_type", "created_dt")
    model = JanusAuth

    @admin.display(ordering="user__email", description="User Email")
    def user_email(self, obj):
        return obj.user.email
