from organizations.backends.modeled import ModelInvitation

from print_nanny_webapp.workspaces.models import Workspace


class WorkspaceInvitationBackend(ModelInvitation):
    notification_subject = "workspaces/email/notification_subject.txt"
    notification_body = "workspaces/email/notification_body.html"
    invitation_subject = "workspaces/email/invitation_subject.txt"
    invitation_body = "workspaces/email/invitation_body.html"
    reminder_subject = "workspaces/email/reminder_subject.txt"
    reminder_body = "workspaces/email/reminder_body.html"

    def __init__(self, org_model=Workspace, namespace=None):
        super().__init__(org_model=org_model, namespace=namespace)
        self.invitation_model = (
            self.org_model.invitation_model
        )  # type: OrganizationInvitationBase
