import logging
from django.apps import apps
from django.conf import settings
from .enum import JanusConfigType

logger = logging.getLogger(__name__)


class RTPCapacityException(Exception):
    pass


def get_available_port() -> int:
    # TODO remove hard-coded port after initial migration
    return 5000
    # JanusStream = apps.get_model("devices", "JanusStream")
    # unavailable_ports = JanusStream.objects.filter(
    #     config_type=JanusConfigType.CLOUD
    # ).values("port")
    # available_ports = set(range(*settings.JANUS_CLOUD_RTP_PORT_RANGE)) - set(unavailable_ports)
    # logger.info("get_available_port() num_unavailable=%s first_available=%s",
    #             len(unavailable_ports), available_ports[0])
    # return available_ports[0]
