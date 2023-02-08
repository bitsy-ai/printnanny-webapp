from typing import Any

from django.contrib import admin
from django.http import HttpRequest
from django.db.models import QuerySet
from django_nats_nkeys.services import nsc_add_app

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


def create_nsc_app(
    _modeladmin: admin.ModelAdmin,
    request: HttpRequest,
    queryset: QuerySet[Any],
):
    for obj in queryset:
        nsc_add_app(obj.organization.name, obj.app_name, obj)


@admin.register(PiNatsApp)
class PiNatsAppAdmin(admin.ModelAdmin):
    list_display = ("pi", "app_name", "json", "bearer")
    model = PiNatsApp
    actions = [create_nsc_app]
