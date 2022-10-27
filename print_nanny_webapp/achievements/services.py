import logging

from django.contrib.auth import get_user_model

from print_nanny_webapp.achievements.enum import AchievementType
from print_nanny_webapp.achievements.models import Achievement

UserModel = get_user_model()

logger = logging.getLogger(__name__)


def check_achievements(user: UserModel):
    """
    Checks achievement completion status for user (all achievements)
    """

    # grant Founding Member achievement (if missing)
    if user.is_subscribed:
        obj, created = Achievement.objects.get_or_create(
            user=user, type=AchievementType.FOUNDING_MEMBER
        )
        if created:
            logger.info(
                "Created Achievement. %s for user %s",
                AchievementType.FOUNDING_MEMBER,
                user,
            )
