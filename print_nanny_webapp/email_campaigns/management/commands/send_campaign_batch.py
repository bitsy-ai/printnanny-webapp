from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

import print_nanny_webapp.email_campaigns.services
from print_nanny_webapp.email_campaigns.models import Campaign

User = get_user_model()


class Command(BaseCommand):
    help = "Send email campaign with batch size"

    def add_arguments(self, parser):
        parser.add_argument("--limit", type=int, default=10)
        parser.add_argument("--template", type=str, required=True)

    def handle(self, *args, **options):
        template = options["template"]
        limit = options["limit"]
        app = options["app"]
        model_str = options["model"]

        campaign = Campaign.objects.get(template=template)
        fn_name = campaign.send_fn.split(".")[-1]
        func = getattr(print_nanny_webapp.email_campaigns.services, fn_name)

        func(campaign, limit=limit)
