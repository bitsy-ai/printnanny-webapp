import logging

from django.dispatch import receiver
from django.db.models.signals import post_save
from print_nanny_webapp.events.models import DeviceEvent
from .services import publish_cloudiot_command

logger = logging.getLogger(__name__)


@receiver(post_save, sender=DeviceEvent, dispatch_uid="create_device_link_task")
def publish_device_event(sender, instance: DeviceEvent, created, **kwargs):
    if instance.command:
        logger.info(f"Attempting to publish DeviceEvent to command topic {instance}")
        publish_cloudiot_command(instance)
