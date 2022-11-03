from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from print_nanny_webapp.email_campaigns.services import (
    migrate_surveys_to_email_waitlist,
)

User = get_user_model()


class Command(BaseCommand):
    help = "Send email campaign with batch size"

    def handle(self, *args, **options):
        migrate_surveys_to_email_waitlist()
