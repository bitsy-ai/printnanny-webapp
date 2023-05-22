from django.db import models
from organizations.abstract import (
    AbstractOrganization,
    AbstractOrganizationUser,
    AbstractOrganizationOwner,
    AbstractOrganizationInvitation,
)


class Workspace(AbstractOrganization):
    """Core workspace organization model"""

    pass


class WorkspaceUser(AbstractOrganizationUser):
    """Links a user to the workspace organization"""

    pass


class WorkspaceOwner(AbstractOrganizationOwner):
    """Identifies ONE user, by WorkspaceUser, to be the owner"""

    pass


class WorkspaceInvitation(AbstractOrganizationInvitation):
    """Stores invitations for adding users to workspace organizations"""

    pass
