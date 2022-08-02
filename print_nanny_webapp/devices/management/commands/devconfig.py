import toml
import json
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import HttpRequest

from print_nanny_webapp.devices.api.serializers import ConfigSerializer
from print_nanny_webapp.devices.models import Pi
from print_nanny_webapp.utils.api.service import get_api_config
from print_nanny_webapp.devices.services import build_license_zip

User = get_user_model()


class Command(BaseCommand):
    help = "Generates printnanny.zip for development environment"

    def add_arguments(self, parser):
        parser.add_argument("--email", type=str)
        parser.add_argument("--hostname", type=str)
        parser.add_argument("--out", type=str)
        parser.add_argument("--port", type=int, default=8000)

    def handle(self, *args, **options):
        if settings.DEBUG is not True:
            raise CommandError(
                f"Refusing to generate test printnanny.zip because settings.DEBUG={settings.DEBUG} (must be True)"
            )
        user = User.objects.get(email=options["email"])  # type: ignore
        self.stdout.write(f"Generating license.json with credentials for user={user}")
        device, created = Pi.objects.get_or_create(
            user=user, hostname=options["hostname"]
        )
        self.stdout.write(
            f"Generating printnanny.zip with device={device} created={created}"
        )
        request = HttpRequest()
        request.user = user
        request.META["HTTP_HOST"] = f"{options['hostname']}:{options['port']}"

        zipdata = build_license_zip(device, request)
        with open(options["out"], "wb+") as f:
            f.write(zipdata)
        self.stdout.write(self.style.SUCCESS(f"Created {options['out']}"))
