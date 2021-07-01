from print_nanny_webapp.subscriptions.models import MemberBadge
from django.apps import apps
from django.contrib import admin

# Register your models here.
MemberBadge = apps.get_model("subscriptions", "MemberBadge")


@admin.register(MemberBadge)
class MemberBadgeAdmin(admin.ModelAdmin):
    list_display = (
        "created_dt",
        "user",
        "type",
    )
