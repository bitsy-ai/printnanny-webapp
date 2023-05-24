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
        self.invitation_model = self.org_model.invitation_model

    def send_invitation(self, invitation, **kwargs):
        """
        Sends an invitation message for a specific invitation.

        This could be overridden to do other things, such as sending a confirmation
        email to the sender.

        Args:
            invitation:

        Returns:

        """
        return self.email_message(
            invitation.invitee_identifier,
            self.invitation_subject,
            self.invitation_body,
            sender=invitation.invited_by,
            invitation=invitation,
        ).send()
