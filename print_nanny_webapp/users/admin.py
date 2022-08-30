from typing import Any
from django.contrib import admin
from django.apps import apps
from django.db.models import QuerySet
from django.http import HttpRequest
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from invitations.utils import get_invitation_model

from rest_framework.authtoken.models import Token
from print_nanny_webapp.users.forms import (
    GroupAdminForm,
)

User = get_user_model()

Invitation = get_invitation_model()

# https://stackoverflow.com/a/39648244
# Unregister the original Group admin.
admin.site.unregister(Group)

# Create a new Group admin.
class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ["permissions"]


# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)

MemberBadge = apps.get_model("subscriptions", "MemberBadge")
EmailWaitlist = apps.get_model("users", "EmailWaitlist")


def create_token(
    _modeladmin,
    request: HttpRequest,
    queryset: QuerySet[Any],
):
    for user in queryset:
        Token.objects.get_or_create(user=user)


def add_free_beta(
    _modeladmin,
    request: HttpRequest,
    queryset: QuerySet[Any],
):

    for user in queryset:
        MemberBadge.objects.create(
            user=user, type=MemberBadge.MemberBadgeType.FREE_BETA
        )


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    # django-loginas
    change_form_template = "loginas/change_form.html"

    # add_form = UserCreationForm
    # form = UserChangeForm
    model = User
    list_display = (
        "email",
        "first_name",
        "last_name",
        "last_login",
        "is_free_beta_tester",
        "is_paid_beta_tester",
        "is_serviceuser",
        "auth_token",
    )
    list_filter = ("email", "is_staff", "is_superuser")
    readonly_fields = ("is_free_beta_tester", "is_paid_beta_tester", "auth_token")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                    "is_free_beta_tester",
                    "is_paid_beta_tester",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_serviceuser")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_serviceuser",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

    actions = [create_token, add_free_beta]


def send_beta_invite(
    _modeladmin: admin.ModelAdmin,
    request: HttpRequest,
    queryset: QuerySet[Any],
):
    for invite_request in queryset:
        invite = Invitation.create(invite_request.email)
        invite.send_invitation(request)
        invite_request.invited = True
        invite_request.save()


@admin.register(EmailWaitlist)
class EmailWaitlistAdmin(admin.ModelAdmin):

    list_filter = ("email",)

    list_display = (
        "email",
        "created_dt",
    )

    actions = [send_beta_invite]
