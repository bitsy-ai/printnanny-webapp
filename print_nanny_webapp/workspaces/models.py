from django.db import models
from django.db.models import QuerySet

from organizations.abstract import (
    AbstractOrganization,
    AbstractOrganizationUser,
    AbstractOrganizationOwner,
    AbstractOrganizationInvitation,
)


class WorkspaceUser(AbstractOrganizationUser):
    """Links a user to the workspace organization"""

    pass


class WorkspaceOwner(AbstractOrganizationOwner):
    """Identifies ONE user, by WorkspaceUser, to be the owner"""

    pass


class WorkspaceInvitation(AbstractOrganizationInvitation):
    """Stores invitations for adding users to workspace organizations"""

    pass


class Workspace(AbstractOrganization):
    """Core workspace organization model"""

    invitation_model = WorkspaceInvitation

    @property
    def pending_invites(self) -> QuerySet[WorkspaceInvitation]:
        """
        Return all invitations with incomplete registration
        """
        return self.invitation_model.objects.filter(
            organization=self, invitee=None
        ).all()
