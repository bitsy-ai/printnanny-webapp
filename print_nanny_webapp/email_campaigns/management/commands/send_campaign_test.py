from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

import print_nanny_webapp.email_campaigns.services
from print_nanny_webapp.email_campaigns.models import Campaign

User = get_user_model()


class Command(BaseCommand):
    help = "Starts a test email campaign"

    def add_arguments(self, parser):
        parser.add_argument("--email", type=str, required=True)
        parser.add_argument("--template", type=str, required=True)

    def handle(self, *args, **options):
        email = options["email"]
        template = options["template"]

        campaign = Campaign.objects.get(template=template)

        fn_name = campaign.send_fn.split(".")[-1]
        func = getattr(print_nanny_webapp.email_campaigns.services, fn_name)

        func(campaign, limit=1, filter_fn=lambda _campaign, _limit=10: email)
