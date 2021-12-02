from config.settings.base import PAID_BETA_SUBSCRIPTION_LIMIT
import djstripe.models
import djstripe.enums
from django.conf import settings
from djstripe.settings import STRIPE_PUBLIC_KEY
from django.utils import timezone


def help_context(_request):
    return {
        "HELP_WIKI_URL": settings.HELP_WIKI_URL,
        "HELP_ACTIVATE_LICENSE": "https://www.notion.so/bitsy-ai/License-Activation-Failed-99bb98ebc01546979717da214d2198c8",
        "ABOUT_DEVICE_PKI": "https://www.notion.so/bitsy-ai/Securing-IoT-Devices-with-PKI-f9e728fb1e734e6d95efb930d9f23620",
    }


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
    return {
        "DEBUG": settings.DEBUG,
        "GOOGLE_ANALYTICS": settings.GOOGLE_ANALYTICS,
        "WS_BASE_URL": settings.WS_BASE_URL,
        "DISCORD_URL": settings.DISCORD_URL,
        "REPORT_ISSUE_URL": settings.REPORT_ISSUE_URL,
        "HELP_SITE_URL": settings.HELP_SITE_URL,
        "ABOUT_URL": settings.ABOUT_URL,
        "BLOG_SITE_URL": settings.BLOG_SITE_URL,
        "HELP_OCTOPRINT_PLUGIN_SETUP": settings.HELP_OCTOPRINT_PLUGIN_SETUP,
        "HELP_PRINTNANNY_OS_SETUP": settings.HELP_PRINTNANNY_OS_SETUP,
        "IS_SOLD_OUT": sold_out,
        "AVAILABLE_SUBSCRIPTIONS_COUNT": num_subscriptions_available,
        "PAID_BETA_SUBSCRIPTION_LIMIT": PAID_BETA_SUBSCRIPTION_LIMIT,
        "STRIPE_PUBLIC_KEY": STRIPE_PUBLIC_KEY,
        "CURRENT_UTC_TS": int(timezone.now().timestamp()),
        "PAID_BETA_LAUNCH_TIMESTAMP": int(settings.PAID_BETA_LAUNCH_TIMESTAMP),
    }
