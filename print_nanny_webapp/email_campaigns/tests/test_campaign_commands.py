from django.test import TestCase
from django.core.management import call_command
from django.test.utils import override_settings

from print_nanny_webapp.users.models import EmailWaitlist
from print_nanny_webapp.email_campaigns.models import EmailMessage


@override_settings(EMAIL_BACKEND="anymail.backends.test.EmailBackend")
class TestCommand(TestCase):
    fixtures = [
        "/app/print_nanny_webapp/email_campaigns/fixtures/email_campaigns.json",
    ]

    def setUp(self) -> None:
        super().setUp()
        self.emails = [
            "john.doe1@example.com",
            "john.doe2@example.com",
            "john.doe3@example.com",
            "john.doe4@example.com",
            "john.doe5@example.com",
            "john.doe6@example.com",
            "john.doe7@example.com",
            "john.doe8@example.com",
            "john.doe9@example.com",
            "john.doe10@example.com",
            "john.doe11@example.com",
        ]
        self.template = "founding-member-offer-1-nov-2022"
        for email in self.emails:
            EmailWaitlist.objects.create(email=email)

    def test_send_campaign_batch__fn_founding_member_november_2022_offer(self):
        # calling command once should send first 10 emails
        call_command("send_campaign_batch", "--template", self.template)
        msg_log = EmailMessage.objects.all()
        assert msg_log.count() == 10
        # calling command against should only send 1 email
        call_command("send_campaign_batch", "--template", self.template)
        msg_log = EmailMessage.objects.all()
        assert msg_log.count() == 11
        # calling command against should only send 0 email
        call_command("send_campaign_batch", "--template", self.template)
        msg_log = EmailMessage.objects.all()
        assert msg_log.count() == 11
