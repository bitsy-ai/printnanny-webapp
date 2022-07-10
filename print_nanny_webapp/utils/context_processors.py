import logging

import djstripe.models
import djstripe.enums
from django.conf import settings
from django.utils import timezone
from djstripe.settings import djstripe_settings
from config.settings.base import PAID_BETA_SUBSCRIPTION_LIMIT

logger = logging.getLogger(__name__)


def settings_context(_request):
    """Settings available by default to the templates context."""
    # Note: we intentionally do NOT expose the entire settings
    # to prevent accidental leaking of sensitive information
    num_subscriptions = djstripe.models.Subscription.objects.filter(
        status=djstripe.enums.SubscriptionStatus.active
    ).count()

    sold_out = num_subscriptions >= settings.PAID_BETA_SUBSCRIPTION_LIMIT

    num_subscriptions_available = int(
        settings.PAID_BETA_SUBSCRIPTION_LIMIT - num_subscriptions
    )

    obj = {
        "ABOUT_URL": settings.ABOUT_URL,
        "API_VERSION": settings.API_VERSION,
        "AVAILABLE_SUBSCRIPTIONS_COUNT": num_subscriptions_available,
        "GIT_SHA": settings.GIT_SHA,
        "CDN_BASE_URL": settings.CDN_BASE_URL,
        "CURRENT_UTC_TS": int(timezone.now().timestamp()),
        "DEBUG": settings.DEBUG,
        "DEMO_VIDEOS": [
            "https://cdn.printnanny.ai/www/demo-video-1.mp4",
            "https://cdn.printnanny.ai/www/demo-video-2.mp4",
            "https://cdn.printnanny.ai/www/demo-video-3.mp4",
            "https://cdn.printnanny.ai/www/demo-video-4.mp4",
        ],
        "DOCS_SITE_URL": settings.DOCS_SITE_URL,
        "DOCS_SITE__QUICKSTART": settings.DOCS_SITE__QUICKSTART,
        "DISCORD_URL": settings.DISCORD_URL,
        "GOOGLE_ANALYTICS": settings.GOOGLE_ANALYTICS,
        "IS_SOLD_OUT": sold_out,
        "PAID_BETA_LAUNCH_TIMESTAMP": int(settings.PAID_BETA_LAUNCH_TIMESTAMP),
        "PAID_BETA_SUBSCRIPTION_LIMIT": PAID_BETA_SUBSCRIPTION_LIMIT,
        "POSTHOG_API_KEY": settings.POSTHOG_API_KEY,
        "PRINTNANNY_OS_RELEASE_URL": settings.PRINTNANNY_OS_RELEASE_URL,
        "PRINTNANNY_OS_INSTALL_URL": settings.PRINTNANNY_OS_INSTALL_URL,
        "STRIPE_PUBLIC_KEY": djstripe_settings.STRIPE_PUBLIC_KEY,
        "WS_BASE_URL": settings.WS_BASE_URL,
    }
    return obj
