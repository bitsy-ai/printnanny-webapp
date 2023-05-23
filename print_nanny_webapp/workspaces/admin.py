from django.contrib import admin

from organizations.models import Organization, OrganizationUser, OrganizationOwner
from organizations.base_admin import BaseOrganizationAdmin
from organizations.base_admin import BaseOrganizationOwnerAdmin
from organizations.base_admin import BaseOrganizationUserAdmin
from organizations.base_admin import BaseOwnerInline
from print_nanny_webapp.workspaces.models import (
    Workspace,
    WorkspaceOwner,
    WorkspaceUser,
    WorkspaceInvitation,
)


class OwnerInline(BaseOwnerInline):
    model = WorkspaceOwner


@admin.register(Workspace)
class WorkspaceAdmin(BaseOrganizationAdmin):
    inlines = [OwnerInline]


@admin.register(WorkspaceUser)
class WorkspaceUserAdmin(BaseOrganizationUserAdmin):
    pass


@admin.register(WorkspaceOwner)
class WorkspaceOwnerAdmin(BaseOrganizationOwnerAdmin):
    pass


@admin.register(WorkspaceInvitation)
class WorkspaceInvitationAdmin(admin.ModelAdmin):
    pass
