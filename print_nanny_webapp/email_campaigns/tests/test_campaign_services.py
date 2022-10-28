from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test.utils import override_settings
from print_nanny_webapp.email_campaigns.services import (
    send_fn_founding_member_november_2022_offer,
)
from print_nanny_webapp.email_campaigns.models import Campaign, EmailMessage

User = get_user_model()


@override_settings(EMAIL_BACKEND="anymail.backends.test.EmailBackend")
class CampaignTestCase(TestCase):

    fixtures = [
        "/app/print_nanny_webapp/email_campaigns/fixtures/email_campaigns.json",
    ]
    #
    def test_send_fn_founding_member_november_2022_offer(self):
        email1 = "john.doe1@example.com"
        email2 = "john.doe2@example.com"

        password = "testing1234"
        # test provided email already associated with an existing stripe customer
        User.objects.create(  # type: ignore[has-type]
            email=email1, password=password, is_superuser=False
        )
        User.objects.create(  # type: ignore[has-type]
            email=email2, password=password, is_superuser=False
        )

        queryset = User.objects.all()  # type: ignore[has-type]
        campaign = Campaign.objects.get(template="founding-member-offer-1-nov-2022")
        msg = send_fn_founding_member_november_2022_offer(queryset, campaign)

        for email, recipient in msg.anymail_status.recipients.items():
            user = User.objects.get(email=email)  # type: ignore[has-type]
            sent_log = EmailMessage.objects.get(
                campaign=campaign, message_id=msg.anymail_status.message_id, user=user
            )

            assert recipient.status == sent_log.send_status
