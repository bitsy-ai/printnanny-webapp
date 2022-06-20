import json
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import HttpRequest

from print_nanny_webapp.devices.api.serializers import LicenseSerializer
from print_nanny_webapp.devices.models import Device
from print_nanny_webapp.utils.api.service import get_api_config

User = get_user_model()


class Command(BaseCommand):
    help = "Generates a license.json for development environment"

    def add_arguments(self, parser):
        parser.add_argument("--email", type=str)
        parser.add_argument("--hostname", type=str)
        parser.add_argument("--out", type=str)
        parser.add_argument("--port", type=int, default=8000)

    def handle(self, *args, **options):
        if settings.DEBUG is not True:
            raise CommandError(
                f"Refusing to generate test license.json because settings.DEBUG={settings.DEBUG} (must be True)"
            )
        user = User.objects.get(email=options["email"])  # type: ignore
        self.stdout.write(f"Generating license.json with credentials for user={user}")
        device, created = Device.objects.get_or_create(
            user=user, hostname=options["hostname"]
        )
        self.stdout.write(
            f"Generating license.json with device={device} created={created}"
        )
        request = HttpRequest()
        request.user = user
        request.META["HTTP_HOST"] = f"{options['hostname']}:{options['port']}"

        api = get_api_config(request, user=user)
        instance = dict(device=device, api=api)
        serializer = LicenseSerializer(instance=instance)
        with open(options["out"], "w") as f:
            json.dump(serializer.data, f)
        self.stdout.write(self.style.SUCCESS(f"Created {options['out']}"))
