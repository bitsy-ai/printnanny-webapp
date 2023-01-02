from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.conf import settings

from drfpasswordless.models import CallbackToken

User = get_user_model()


class Command(BaseCommand):
    help = "Gets callback token for user 2fa, used for e2e test suite"

    def add_arguments(self, parser):
        parser.add_argument("--email", type=str, required=True)

    def handle(self, *args, **options):
        if settings.DEBUG is not True:
            raise CommandError(
                f"Refusing to fetch 2fa auth token because settings.DEBUG={settings.DEBUG} (must be True)"
            )
        email = options["email"]
        user = User.objects.get(email=email)
        token = CallbackToken.objects.filter(user=user).order_by("-created_at").first()
        self.stdout.write(self.style.SUCCESS(f"Callback token for {email}:"))
        self.stdout.write(token.key)
