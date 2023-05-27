import pytest

from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.exceptions import PermissionDenied

from print_nanny_webapp.devices.models import Pi
from print_nanny_webapp.devices.enum import (
    JanusConfigType,
    SingleBoardComputerType,
    PreferredDnsType,
)
from print_nanny_webapp.workspaces.models import (
    WorkspaceOwner,
    WorkspaceUser,
    Workspace,
)
from print_nanny_webapp.workspaces.services import (
    create_personal_workspace,
    assign_pi_to_workspace,
)

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

    def test_assign_pi(self):
        email = "dora.stone@rapidmanufacturingexample.com"
        first_name = "Dora"
        last_name = "Stone"
        user = User.objects.create(
            email=email, is_superuser=False, first_name=first_name, last_name=last_name
        )

        pi = Pi.objects.create(
            sbc=SingleBoardComputerType.RPI_4,
            hostname="testpi",
            user=user,
            favorite=True,
            setup_finished=True,
        )

        workspace = Workspace.objects.create(name="testworkspace", slug="testworkspace")

        # should fail, user isn't a member of workspace
        with pytest.raises(PermissionDenied):
            assign_pi_to_workspace(pi.id, workspace.id, user)

        workspace.get_or_add_user(user)
        # should succeeed, user is now owner of workspace
        result = assign_pi_to_workspace(pi.id, workspace.id, user)
        assert result.workspace.id == workspace.id
