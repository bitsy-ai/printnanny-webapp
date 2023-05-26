# creates a default workspace for each user
import logging

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from print_nanny_webapp.workspaces.services import create_personal_workspace


logger = logging.getLogger(__name__)

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # get all users who are not owners of a personal workspace

        O.objects.filter()
