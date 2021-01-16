from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from print_nanny_webapp.users.forms import UserChangeForm, UserCreationForm
from print_nanny_webapp.users.models import InviteRequest
from invitations.utils import get_invitation_model

User = get_user_model()

Invitation = get_invitation_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ("email", "is_staff", "is_active", "is_superuser")
    list_filter = ("email", "is_staff", "is_active", "is_superuser")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


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
