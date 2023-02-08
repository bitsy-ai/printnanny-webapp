from django.contrib import admin
from print_nanny_webapp.devices.models import Pi, WebrtcStream, PiNatsApp


@admin.register(Pi)
class PiAdmin(admin.ModelAdmin):
    list_display = ("hostname", "user", "created_dt")
    model = Pi


@admin.register(WebrtcStream)
class WebrtcStreamAdmin(admin.ModelAdmin):
    list_display = (
        "pi",
        "pi_hostname",
        "active",
        "config_type",
        "created_dt",
    )
    model = WebrtcStream

    @admin.display(ordering="pi__hostname", description="Pi Hostname")
    def pi_hostname(self, obj):
        return obj.pi.hostname


@admin.register(PiNatsApp)
class PiNatsAppAdmin(admin.ModelAdmin):
    list_display = ("pi", "app_name", "json", "bearer")
    model = PiNatsApp
