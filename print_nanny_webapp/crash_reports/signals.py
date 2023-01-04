import logging

from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
import requests

from print_nanny_webapp.crash_reports.models import CrashReport

logger = logging.getLogger(__name__)

User = get_user_model()


@receiver(post_save, sender=CrashReport)
def crash_report_to_discord_webhook(sender, instance, created, **kwargs):
    # only send when report is created for the first time
    if created:
        if (
            settings.DISCORD_NEW_SIGNUP_WEBHOOK is not None
            and settings.DEBUG is not True
        ):
            url = instance.get_admin_url()
            body = {"content": f"🐛 New Crash Report: {url}"}
            requests.post(settings.DISCORD_NEW_SIGNUP_WEBHOOK, json=body, timeout=300)


@receiver(post_save, sender=CrashReport)
def try_associate_user(sender, instance, **kwargs):
    # if instance.user is not set, attempt to build the association by email address
    if instance.user is None:
        user = User.objects.filter(email=instance.email).first()
        if user is not None:
            instance.user = user
            instance.save()
        else:
            logger.error(
                "Received crash report from email=%s but no user is associated with email",
                instance.email,
            )
