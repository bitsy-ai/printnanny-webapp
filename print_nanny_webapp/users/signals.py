from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
import requests

from print_nanny_webapp.users.models import EmailWaitlist


@receiver(post_save, sender=EmailWaitlist)
def email_waitlist_to_discord_webhook(sender, instance, **kwargs):
    if settings.DISCORD_NEW_SIGNUP_WEBHOOK is not None:
        body = {"content": f"{instance.email} added to waitlist 🎉"}
        requests.post(settings.DISCORD_NEW_SIGNUP_WEBHOOK, json=body)
