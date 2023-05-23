from django.db.models.query import QuerySet

from print_nanny_webapp.workspaces.models import Workspace, WorkspaceUser


def get_workspaces_by_auth_user(user) -> QuerySet[Workspace]:
    workspace_users = WorkspaceUser.objects.filter(user=user)
    return [u.organization for u in workspace_users]
