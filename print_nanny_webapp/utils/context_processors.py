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
        "GETTING_STARTED": settings.HELP_GETTING_STARTED,
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

    base_api_url = request.build_absolute_uri("/")[
        :-1
    ]  # remove trailing slash for use in API client base_url

    if "http://" in base_api_url:
        ws_base_url = base_api_url.replace("http://", "ws://")
    elif "https://" in base_api_url:
        ws_base_url = base_api_url.replace("https://", "wss://")
    else:
        raise Exception("Failed to parse base api URL into base ws url")
    ws_base_url = f"{ws_base_url}/ws"
    alerts_ws_url = f"{ws_base_url}/alerts/"
    DEVICE_US_URL = f"{ws_base_url}/alerts/"

    obj = {
        "BASE_API_URL": base_api_url,
        "ALERTS_WS_URL": alerts_ws_url,
        "DEVICE_US_URL": DEVICE_US_URL,
        "DEBUG": settings.DEBUG,
        "GOOGLE_ANALYTICS": settings.GOOGLE_ANALYTICS,
        "WS_BASE_URL": settings.WS_BASE_URL,
        "DISCORD_URL": settings.DISCORD_URL,
        "REPORT_ISSUE_URL": settings.REPORT_ISSUE_URL,
        "HELP_SITE_URL": settings.HELP_SITE_URL,
        "ABOUT_URL": settings.ABOUT_URL,
        "BLOG_SITE_URL": settings.BLOG_SITE_URL,
        "HELP_OCTOPRINT_PLUGIN_SETUP": settings.HELP_OCTOPRINT_PLUGIN_SETUP,
        "IS_SOLD_OUT": sold_out,
        "AVAILABLE_SUBSCRIPTIONS_COUNT": num_subscriptions_available,
        "PAID_BETA_SUBSCRIPTION_LIMIT": PAID_BETA_SUBSCRIPTION_LIMIT,
        "STRIPE_PUBLIC_KEY": STRIPE_PUBLIC_KEY,
        "CURRENT_UTC_TS": int(timezone.now().timestamp()),
        "PAID_BETA_LAUNCH_TIMESTAMP": int(settings.PAID_BETA_LAUNCH_TIMESTAMP),
    }
    return obj
