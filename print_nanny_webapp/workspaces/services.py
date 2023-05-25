from django.db.models.query import QuerySet
from rest_framework.exceptions import PermissionDenied

from print_nanny_webapp.workspaces.models import (
    Workspace,
    WorkspaceUser,
    WorkspaceInvitation,
)


def get_workspaces_by_auth_user(user) -> QuerySet[Workspace]:
    workspace_users = WorkspaceUser.objects.filter(user=user)
    return [u.organization for u in workspace_users]


def verify_workspace_invite(token: str, email: str):
    invite = WorkspaceInvitation.objects.get(guid=token)
    if invite.invitee_identifier == email:
        return invite
    raise PermissionDenied()
