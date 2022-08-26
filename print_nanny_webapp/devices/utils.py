import logging
import random
from typing import List
from django.db.migrations.executor import MigrationExecutor
from django.db import connections, DEFAULT_DB_ALIAS
from django.apps import apps
from django.conf import settings
from print_nanny_webapp.devices.enum import JanusConfigType

logger = logging.getLogger(__name__)


class RTPCapacityException(Exception):
    pass


def is_database_synchronized(database):
    connection = connections[database]
    connection.prepare_database()
    executor = MigrationExecutor(connection)
    targets = executor.loader.graph.leaf_nodes()
    return not executor.migration_plan(targets)


def get_available_rtp_port(portrange: List[int], field: str) -> int:
    if is_database_synchronized(DEFAULT_DB_ALIAS):
        WebrtcStream = apps.get_model("devices", "WebrtcStream")
        unavailable_ports = WebrtcStream.objects.filter(
            config_type=JanusConfigType.CLOUD, deleted=None
        ).values(field)
        logger.info("get_available_port() reserved_ports %s", unavailable_ports)
        logger.info(
            "get_available_port() settings.JANUS_CLOUD_VIDEO_RTP_PORT_RANGE %s",
            settings.JANUS_CLOUD_VIDEO_RTP_PORT_RANGE,
        )
        available_ports = set(portrange) - set((x[field] for x in unavailable_ports))
        first_available = available_ports.pop()
        logger.info(
            "get_available_port() num_unavailable=%s first_available=%s",
            len(unavailable_ports),
            first_available,
        )
        return int(first_available)
    else:
        logger.warning(
            "Database is not synchronized in get_available_port() - returning a random port"
        )
        return random.choice(portrange)


def get_available_video_rtp_port() -> int:
    portrange = list(range(*settings.JANUS_CLOUD_VIDEO_RTP_PORT_RANGE))
    args = (portrange, "video_rtp_port")
    return get_available_rtp_port(*args)


def get_available_data_rtp_port() -> int:
    portrange = list(range(*settings.JANUS_CLOUD_DATA_RTP_PORT_RANGE))
    args = (portrange, "data_rtp_port")
    return get_available_rtp_port(*args)
