import logging

from django.dispatch import receiver
from django.db.models.signals import post_save
from print_nanny_webapp.events.models import DeviceEvent
from .services import Device, publish_cloudiot_command

logger = logging.getLogger(__name__)


@receiver(post_save, dispatch_uid="publish_device_event_command_topic")
def publish_device_event(sender, instance, created, **kwargs):
    logger.info(f"Saved DeviceEvent {instance}")
    if isinstance(instance, DeviceEvent):
        logger.info(f"Attempting to publish DeviceEvent to command topic {instance}")
        publish_cloudiot_command(instance)
