from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

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
        queryset = User.objects.filter(email=email)

        module_name = campaign.send_fn.split(".")[0:-1].join(".")
        module = __import__(module_name)
        fn_name = campaign.send_fn.split(".")[-1]
        func = getattr(module, fn_name)

        func(queryset, campaign)
