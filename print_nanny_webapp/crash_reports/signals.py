import logging

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
import requests

from print_nanny_webapp.crash_reports.models import CrashReport

logger = logging.getLogger(__name__)


@receiver(post_save, sender=CrashReport)
def crash_report_to_discord_webhook(sender, instance, **kwargs):
    if settings.DISCORD_NEW_SIGNUP_WEBHOOK is not None and settings.DEBUG is not True:
        url = instance.get_admin_url()
        body = {"content": f"🐛 New Crash Report: {url}"}
        requests.post(settings.DISCORD_NEW_SIGNUP_WEBHOOK, json=body, timeout=300)
