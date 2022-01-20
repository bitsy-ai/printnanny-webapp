import logging
from config.settings.base import PAID_BETA_SUBSCRIPTION_LIMIT
import djstripe.models
import djstripe.enums
from django.conf import settings
from djstripe.settings import STRIPE_PUBLIC_KEY
from django.utils import timezone

logger = logging.getLogger(__name__)


def help_context(_request):
    return {
        "HELP_WIKI_URL": settings.HELP_WIKI,
        "ERROR_ACTIVATE_LICENSE": settings.ERROR_ACTIVATE_LICENSE,
        "DEVICE_PKI": settings.HELP_DEVICE_PKI,
        "HELP_GETTING_STARTED": settings.HELP_GETTING_STARTED,
        "ROADMAP_URL": settings.ROADMAP_URL,
    }


def settings_context(request):
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
        "AVAILABLE_SUBSCRIPTIONS_COUNT": num_subscriptions_available,
        "BLOG_SITE_URL": settings.BLOG_SITE_URL,
        "CDN_BASE_URL": settings.CDN_BASE_URL,
        "CURRENT_UTC_TS": int(timezone.now().timestamp()),
        "DEBUG": settings.DEBUG,
        "DEMO_VIDEOS": [
            "https://cdn.print-nanny.com/www/demo-video-1.mp4",
            "https://cdn.print-nanny.com/www/demo-video-2.mp4",
            "https://cdn.print-nanny.com/www/demo-video-3.mp4",
            "https://cdn.print-nanny.com/www/demo-video-4.mp4",
        ],
        "DISCORD_URL": settings.DISCORD_URL,
        "GOOGLE_ANALYTICS": settings.GOOGLE_ANALYTICS,
        "HELP_OCTOPRINT_PLUGIN_SETUP": settings.HELP_OCTOPRINT_PLUGIN_SETUP,
        "HELP_SITE_URL": settings.HELP_SITE_URL,
        "IS_SOLD_OUT": sold_out,
        "PAID_BETA_LAUNCH_TIMESTAMP": int(settings.PAID_BETA_LAUNCH_TIMESTAMP),
        "PAID_BETA_SUBSCRIPTION_LIMIT": PAID_BETA_SUBSCRIPTION_LIMIT,
        "POSTHOG_API_KEY": settings.POSTHOG_API_KEY,
        "REPORT_ISSUE_URL": settings.REPORT_ISSUE_URL,
        "ROADMAP_URL": settings.ROADMAP_URL,
        "STRIPE_PUBLIC_KEY": STRIPE_PUBLIC_KEY,
        "WS_BASE_URL": settings.WS_BASE_URL,
    }
    return obj
