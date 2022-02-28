from django.contrib import admin

from print_nanny_webapp.referrals.forms import (
    ReferralInviteCreateForm,
    ReferralCodeCreateForm,
)
from print_nanny_webapp.referrals.models import ReferralCode, ReferralInvite

# Register your models here.


@admin.register(ReferralCode)
class ReferralCodeAdmin(admin.ModelAdmin):
    add_form = ReferralCodeCreateForm
    model = ReferralCode

    change_form_template = "qrcode_change_form.html"


class ReferralInviteAdmin(admin.ModelAdmin):
    add_form = ReferralInviteCreateForm
    model = ReferralInvite
