import logging

from django.conf import settings

from djstripe.models import Customer
from print_nanny_webapp.achievements.enum import AchievementType
from print_nanny_webapp.achievements.models import Achievement

logger = logging.getLogger(__name__)


def check_achievements(user):
    """
    Checks achievement completion status for user (all achievements)
    """

    # grant Founding Member achievement (if missing)
    if user.is_subscribed:
        # get active subscription
        try:
            customer = Customer.objects.get(subscriber=user)
        except Customer.DoesNotExist:
            logger.error(
                "check_achievements failed to get Stripe Customer for user=%s", user
            )
            return
        subscriptions = customer.subscriptions.all()
        for subscription in subscriptions:
            # we didn't know about price_ids when settings up Founding Memberships, so filter on the nickname
            if "Founding Member" in subscription.plan.nickname:
                obj, created = Achievement.objects.get_or_create(
                    user=user, type=AchievementType.FOUNDING_MEMBER
                )
                if created:
                    logger.info(
                        "Created Achievement. %s for user %s",
                        obj,
                        user,
                    )

            elif subscription.plan.product.id == settings.STRIPE_STARTER_PRODUCT_ID:
                obj, created = Achievement.objects.get_or_create(
                    user=user, type=AchievementType.CLOUD_STARTER
                )
                if created:
                    logger.info(
                        "Created Achievement. %s for user %s",
                        obj,
                        user,
                    )
            elif subscription.plan.product.id == settings.STRIPE_SCALER_PRODUCT_ID:
                obj, created = Achievement.objects.get_or_create(
                    user=user, type=AchievementType.CLOUD_SCALER
                )
                if created:
                    logger.info(
                        "Created Achievement. %s for user %s",
                        obj,
                        user,
                    )
