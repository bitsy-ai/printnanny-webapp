import logging

from print_nanny_webapp.events.models import DeviceEvent
from .services import publish_cloudiot_event

logger = logging.getLogger(__name__)


def publish_device_event(sender, instance: DeviceEvent, created, **kwargs):
    return publish_cloudiot_event(instance)
