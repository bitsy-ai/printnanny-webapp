from django.test import TestCase
from django.contrib.auth import get_user_model

from print_nanny_webapp.workspaces.models import WorkspaceOwner, WorkspaceUser
from print_nanny_webapp.workspaces.services import create_personal_workspace

User = get_user_model()


class WorkspacesSignalTestCase(TestCase):
    def test_personal_workspace_created_by_firstlast_name(self):
        email = "dora.stone@rapidmanufacturingexample.com"
        first_name = "Dora"
        last_name = "Stone"
        user = User.objects.create(
            email=email, is_superuser=False, first_name=first_name, last_name=last_name
        )

        workspace_user = WorkspaceUser.objects.get(user=user)
        assert workspace_user.organization.name == "Dora Stone's Workspace"
        assert workspace_user.organization.is_owner(user)

    def test_personal_workspace_created_by_email(self):
        email = "brock.stone@rapidmanufacturingexample.com"
        user = User.objects.create(email=email, is_superuser=False)

        workspace_user = WorkspaceUser.objects.get(user=user)

        assert (
            workspace_user.organization.name
            == "brock.stone@rapidmanufacturingexample.com's Workspace"
        )
        assert workspace_user.organization.is_owner(user)
