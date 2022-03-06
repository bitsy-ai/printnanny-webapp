from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from rest_framework.authtoken.models import Token
from print_nanny_webapp.users.forms import (
    UserChangeForm,
    UserCreationForm,
    GroupAdminForm,
)
from print_nanny_webapp.users.models import InviteRequest
from invitations.utils import get_invitation_model

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


def create_token(modeladmin, request, queryset):
    for user in queryset:
        Token.objects.get_or_create(user=user)


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
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

    actions = [create_token]


def send_beta_invite(modeladmin, request, queryset):
    for invite_request in queryset:
        invite = Invitation.create(invite_request.email)
        invite.send_invitation(request)
        invite_request.invited = True
        invite_request.save()


@admin.register(InviteRequest)
class InviteRequestAdmin(admin.ModelAdmin):

    list_filter = ("email",)

    list_filters = ("invited", "email")
    list_display = (
        "first_name",
        "invited",
        "last_name",
        "email",
        "created_dt",
    )

    actions = [send_beta_invite]
