from django.contrib import admin

from print_nanny_webapp.referrals.forms import (
    ReferralInviteCreateForm,
    ReferralCodeCreateForm,
)
from print_nanny_webapp.referrals.models import ReferralCode, ReferralInvite

# Register your models here.


def generate_referral_qrcode(modeladmin, request, queryset):
    pass


def send_referral_email(modeladmin, request, queryset):
    pass


@admin.register(ReferralCode)
class ReferralCodeAdmin(admin.ModelAdmin):
    add_form = ReferralCodeCreateForm
    model = ReferralCode

    actions = [generate_referral_qrcode]
    change_form_template = "qrcode_change_form.html"


class ReferralInviteAdmin(admin.ModelAdmin):
    add_form = ReferralInviteCreateForm
    model = ReferralInvite
    actions = [send_referral_email]
