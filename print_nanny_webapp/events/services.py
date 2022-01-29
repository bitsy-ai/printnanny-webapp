import logging

from django.apps import apps
from rest_framework.renderers import JSONRenderer
from google.cloud import iot_v1 as cloudiot_v1
from print_nanny_webapp.events.api.serializers import PolymorphicEventSerializer

Device = apps.get_model("devices", "Device")
DeviceEvent = apps.get_model("events", "DeviceEvent")

logger = logging.getLogger(__name__)


def publish_cloudiot_command(event: DeviceEvent):
    device: Device = event.device
    serializer = PolymorphicEventSerializer(instance=event)
    data = JSONRenderer().render(serializer.data)
    request = cloudiot_v1.types.SendCommandToDeviceRequest(
        {
            "name": device.cloudiot.gcp_resource,
            "binary_data": data,
            # NOTE "subfolder" may be added to publish to a subfolder
            # "subfolder": device.cloudiot.event_topic,
        }
    )

    response = device.cloudiot.client.send_command_to_device(request=request)
    logger.info(f"cloudiot.client.send_command_to_device response {response}")
    return response
