import logging
from django.core.management.base import BaseCommand

from print_nanny_webapp.devices.services import janus_stream_clean

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Destroys Janus stream mountpoints with 0 users and de-allocates UDP ports"

    def add_arguments(self, parser):
        parser.add_argument(
            "--max-age-seconds", default=3600, help="Max streage (in seconds)"
        )

    def handle(self, *args, **options):
        janus_stream_clean()
