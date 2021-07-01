import logging
from print_nanny_webapp.subscriptions.models import MemberBadge
from celery import shared_task
from django.apps import apps
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models import Q

logger = logging.getLogger(__name__)

User = get_user_model()
MemberBadge = apps.get_model("subscriptions", "MemberBadge")


@shared_task
def create_free_beta_tester_badges():
    max_id = list(settings.FREE_BETA_TESTER_IDS)[-1]
    users = User.objects.filter(Q(id__lte=max_id))
    for user in users:
        obj, created = MemberBadge.get_or_create(
            user=user, type=MemberBadge.Types.FREE_BETA
        )
        if created:
            logger.info(f"Created new {obj}")
        else:
            logger.info(f"Skipping existing {obj}")
