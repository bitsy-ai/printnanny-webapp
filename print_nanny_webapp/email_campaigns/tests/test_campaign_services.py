from anymail.signals import AnymailTrackingEvent, tracking

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test.utils import override_settings
from print_nanny_webapp.email_campaigns.models import (
    EmailTrackingEvent,
)
from print_nanny_webapp.email_campaigns.models import Campaign, EmailMessage
from print_nanny_webapp.email_campaigns.services import (
    send_fn_founding_member_november_2022_offer,
)
from print_nanny_webapp.users.models import EmailWaitlist

User = get_user_model()


@override_settings(EMAIL_BACKEND="anymail.backends.test.EmailBackend")
class CampaignTestCase(TestCase):

    fixtures = [
        "/app/print_nanny_webapp/email_campaigns/fixtures/email_campaigns.json",
    ]

    def test_log_tracking_event(self):
        # Build an AnymailTrackingEvent with event_type (required)
        # and any other attributes your receiver cares about. E.g.:

        recipient = "to@example.com"
        event_type = "delivered"
        message_id = "test-message-id"

        event = AnymailTrackingEvent(
            event_type=event_type,
            recipient=recipient,
            message_id=message_id,
        )

        # Invoke all registered Anymail tracking signal receivers:
        tracking.send(sender=object(), event=event, esp_name="TestESP")

        self.assertTrue(
            EmailTrackingEvent.objects.filter(
                recipient=recipient, event_type=event_type, message_id=message_id
            ).exists()
        )

    def test_send_fn_founding_member_november_2022_offer(self):

        # test mix of User accounts and EmailWaitlist without User
        emails = [
            "john.doe1@example.com",
            "john.doe2@example.com",
            "john.doe3@example.com",
        ]
        password = "testing1234"
        User.objects.create(  # type: ignore[has-type]
            email=emails[0], password=password, is_superuser=False
        )
        for email in emails[1:]:
            EmailWaitlist.objects.create(email=email)

        campaign = Campaign.objects.get(template="founding-member-november-v2")
        msg = send_fn_founding_member_november_2022_offer(emails, campaign)

        for email, recipient in msg.anymail_status.recipients.items():
            try:
                user = User.objects.get(email=email)  # type: ignore[has-type]
                sent_log = EmailMessage.objects.get(
                    campaign=campaign,
                    message_id=msg.anymail_status.message_id,
                    user=user,
                    email=email,
                )
            except User.DoesNotExist:
                sent_log = EmailMessage.objects.get(
                    campaign=campaign,
                    message_id=msg.anymail_status.message_id,
                    user=None,
                    email=email,
                )

            assert recipient.status == sent_log.send_status
