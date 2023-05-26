from django.db.models.query import QuerySet
from django.utils.text import slugify
from rest_framework.exceptions import PermissionDenied

from print_nanny_webapp.workspaces.models import (
    Workspace,
    WorkspaceUser,
    WorkspaceInvitation,
)


def default_workspace_name(user) -> str:
    if (
        user.first_name is None
        or user.last_name is None
        or user.first_name == ""
        or user.last_name == ""
    ):
        return f"{user.email}'s Workspace"
    else:
        return f"{user.first_name} {user.last_name}'s Workspace"


def get_workspaces_by_auth_user(user) -> QuerySet[Workspace]:
    workspace_users = WorkspaceUser.objects.filter(user=user)
    return [u.organization for u in workspace_users]


def verify_workspace_invite(token: str, email: str):
    invite = WorkspaceInvitation.objects.get(guid=token)
    if invite.invitee_identifier == email:
        return invite
    raise PermissionDenied()


def create_personal_workspace(user) -> Workspace:
    workspace_name = default_workspace_name(user)
    workspace_slug = slugify(workspace_name)
    workspace = Workspace.objects.create(
        slug=workspace_slug, name=workspace_name, is_active=True
    )
    workspace.get_or_add_user(user)
    return workspace
