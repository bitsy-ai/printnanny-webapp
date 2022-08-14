from django.apps import apps
from django.forms import ModelForm
from django.contrib import admin
from print_nanny_webapp.subscriptions.forms import (
    ReferralInviteCreateForm,
    ReferralCodeCreateForm,
)
from print_nanny_webapp.subscriptions.models import ReferralCode, ReferralInvite

# Register your models here.
MemberBadge = apps.get_model("subscriptions", "MemberBadge")


class MemberBadgeForm(ModelForm):
    class Meta:
        model = MemberBadge
        exclude = ["name"]


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
