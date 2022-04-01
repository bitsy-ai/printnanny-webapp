import logging
from django.db.migrations.executor import MigrationExecutor
from django.db import connections, DEFAULT_DB_ALIAS
from django.db.utils import ProgrammingError, InternalError
from django.apps import apps
from django.conf import settings
from .enum import JanusConfigType

logger = logging.getLogger(__name__)


class RTPCapacityException(Exception):
    pass


def is_database_synchronized(database):
    connection = connections[database]
    connection.prepare_database()
    executor = MigrationExecutor(connection)
    targets = executor.loader.graph.leaf_nodes()
    return not executor.migration_plan(targets)


def get_available_rtp_port() -> int:
    if is_database_synchronized(DEFAULT_DB_ALIAS):
        JanusStream = apps.get_model("devices", "JanusStream")
        unavailable_ports = JanusStream.objects.filter(
            config_type=JanusConfigType.CLOUD
        ).values("rtp_port")
        logger.info("get_available_port() reserved_ports %s", unavailable_ports)
        logger.info(
            "get_available_port() settings.JANUS_CLOUD_RTP_PORT_RANGE %s",
            settings.JANUS_CLOUD_RTP_PORT_RANGE,
        )

        available_ports = set(list(range(*settings.JANUS_CLOUD_RTP_PORT_RANGE))) - set(
            x["rtp_port"] for x in unavailable_ports
        )
        first_available = available_ports.pop()
        logger.info(
            "get_available_port() num_unavailable=%s first_available=%s",
            len(unavailable_ports),
            first_available,
        )
        return int(first_available)
    else:
        logger.warning(
            "Database is not synchronized in get_available_port() - returning default of 5001"
        )
        return 5001
