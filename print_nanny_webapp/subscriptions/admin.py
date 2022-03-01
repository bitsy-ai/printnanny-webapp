from django.apps import apps
from django.contrib import admin
from .forms import (
    ReferralInviteCreateForm,
    ReferralCodeCreateForm,
)
from .models import ReferralCode, ReferralInvite

# Register your models here.
MemberBadge = apps.get_model("subscriptions", "MemberBadge")


@admin.register(MemberBadge)
class MemberBadgeAdmin(admin.ModelAdmin):
    list_display = (
        "created_dt",
        "user",
        "type",
    )


@admin.register(ReferralCode)
class ReferralCodeAdmin(admin.ModelAdmin):
    list_display = ("code", "created_dt", "user", "referral_url")
    add_form = ReferralCodeCreateForm
    model = ReferralCode

    change_form_template = "qrcode_change_form.html"


class ReferralInviteAdmin(admin.ModelAdmin):
    add_form = ReferralInviteCreateForm
    model = ReferralInvite
