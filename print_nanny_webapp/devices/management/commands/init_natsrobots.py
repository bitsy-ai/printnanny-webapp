from django.core.management.base import BaseCommand
from print_nanny_webapp.devices.services import init_robots


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        init_robots()
