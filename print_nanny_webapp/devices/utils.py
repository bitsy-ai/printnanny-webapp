import logging
from django.apps import apps
from django.conf import settings
from .enum import JanusConfigType

logger = logging.getLogger(__name__)


class RTPCapacityException(Exception):
    pass


def get_available_port() -> int:
    JanusStream = apps.get_model("devices", "JanusStream")
    unavailable_ports = JanusStream.objects.filter(
        config_type=JanusConfigType.CLOUD
    ).values("rtp_port")
    logger.info("get_available_port() reserved_ports %s", unavailable_ports)
    available_ports = set(list(range(*settings.JANUS_CLOUD_RTP_PORT_RANGE))) - set(
        x["rtp_port"] for x in unavailable_ports
    )
    first_available = available_ports.pop()
    logger.info(
        "get_available_port() num_unavailable=%s first_available=%s",
        len(unavailable_ports),
        first_available,
    )
    return first_available
