import logging
from health_check.backends import BaseHealthCheckBackend
from django.conf import settings
from django.utils import timezone

from google.cloud import monitoring_v3
from google.cloud.monitoring_v3 import query

client = monitoring_v3.MetricServiceClient()
path = client.common_project_path(settings.GCP_PROJECT_ID)
logger = logging.getLogger(__name__)

class RemoteControlEventCheck(BaseHealthCheckBackend):
    #: The status endpoints will respond with a 200 status code
    #: even if the check errors.
    critical_service = False

    def check_status(self):
        pass
    def identifier(self):
        return self.__class__.__name__  # Display name on the endpoint.