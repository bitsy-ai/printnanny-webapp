from typing import List, Any
from django.contrib.sites.models import Site
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from django.urls import path

from organizations.backends.modeled import ModelInvitation

from print_nanny_webapp.workspaces.models import Workspace


class WorkspaceInvitationBackend(ModelInvitation):
    notification_subject = "workspaces/email/notification_subject.txt"
    notification_body = "workspaces/email/notification_body.html"
    invitation_subject = "workspaces/email/invitation_subject.txt"
    invitation_body = "workspaces/email/invitation_body.html"
    invitation_join_template = "index.j2"
    registration_form_template = "index.j2"

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
        current_site = Site.objects.get_current()
        return self.email_message(
            invitation.invitee_identifier,
            self.invitation_subject,
            self.invitation_body,
            sender=invitation.invited_by,
            invitation=invitation,
            site=current_site,
            email=invitation.invitee_identifier,
        ).send()

    def get_urls(self) -> List[Any]:
        return [
            path(
                "<uuid:guid>/<str:email>/",
                view=self.activation_router,
                name="invitations_register",
            )
        ]

    def activation_router(self, request, guid, email):
        """"""
        invitation = get_object_or_404(self.get_invitation_queryset(), guid=guid)
        if invitation.invitee:
            return redirect(self.get_invitation_accepted_url())

        if request.user.is_authenticated:
            return self.activate_existing_user_view(request, invitation)
        else:
            return self.activate_new_user_view(request, invitation)
