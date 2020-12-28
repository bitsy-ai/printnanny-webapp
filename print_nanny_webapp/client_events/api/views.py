
from Crypto.PublicKey import RSA
import logging

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet

from rest_framework.views import APIView
from rest_framework.parsers import (
    MultiPartParser,
    FormParser,
    JSONParser,
    FileUploadParser,
)
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from django.apps import apps
from django.core.files.base import ContentFile
from django.conf import settings

from .serializers import (
    OctoPrintEventSerializer,
    OctoPrintDeviceSerializer
)
from print_nanny_webapp.client_events.models import (
    OctoPrintEvent,
    OctoPrintDevice
)
from google.cloud import iot_v1 as cloudiot_v1

PrintJob = apps.get_model("remote_control", "PrintJob")
logger = logging.getLogger(__name__)


@extend_schema(tags=["events"])
@extend_schema_view(
    create=extend_schema(
        responses={201: OctoPrintEventSerializer, 400: OctoPrintEventSerializer}
    )
)
class OctoPrintEventViewSet(
    CreateModelMixin, GenericViewSet, ListModelMixin, RetrieveModelMixin
):
    serializer_class = OctoPrintEventSerializer
    queryset = OctoPrintEvent.objects.all()
    lookup_field = "id"

    @extend_schema(
        tags=["events"],
        operation_id="octoprint_events_tracking_retrieve",
        responses={200: OpenApiTypes.STR},
    )
    @action(methods=["GET"], detail=False)
    def tracking(self, *args, **kwargs):
        return Response(
            [x.value for x in OctoPrintEvent.EventTypeChoices.__members__.values()],
            status.HTTP_200_OK,
        )

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):

        event_data = self.request.data["event_data"]

        print_job = event_data.get("print_job")
        if print_job is not None:
            print_job = PrintJob.objects.get(id=print_job)
        if self.request.user:
            user = self.request.user
        else:
            user = None
        instance = serializer.save(user=user, print_job=print_job)

@extend_schema(tags=["devices"])
@extend_schema_view(
    create=extend_schema(responses={201: OctoPrintDeviceSerializer, 400: OctoPrintDeviceSerializer})
)
class OctoPrintDeviceViewSet(
    CreateModelMixin, GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
):

    serializer_class = OctoPrintDeviceSerializer
    queryset = OctoPrintDevice.objects.all()
    lookup_field = "id"

    def perform_create(self, serializer):

        key = RSA.generate(2048)

        private_key = key.export_key()
        public_key = key.publickey().export_key()
        
        # https://stackoverflow.com/questions/6682815/deriving-an-ssh-fingerprint-from-a-public-key-in-python

        key = base64.b64decode(self.public_key.strip().split()[1].encode('ascii'))
        fp_plain = hashlib.md5(key).hexdigest()
        fingerprint = ':'.join(a+b for a,b in zip(fp_plain[::2], fp_plain[1::2]))
        
        private_key_content = ContentFile(private_key)
        public_key_content = ContentFile(public_key)
        
        client = cloudiot_v1.DeviceManagerClient()


        parent = client.registry_path(
            settings.GCP_PROJECT_ID, 
            settings.GCP_CLOUD_IOT_DEVICE_REGISTRY_REGION, 
            settings.GCP_CLOUD_IOT_DEVICE_REGISTRY
        )

        device = serializer.save(
            user=self.request.user, 
            private_key=private_key_content, 
            public_key=public_key_content,
            fingerprint=fingerprint
        )

        device_template = {
            "id": device.fingerprint,
            "credentials": [
                {
                    "public_key": {
                        "format": cloudiot_v1.PublicKeyFormat.RSA_X509_PEM,
                        "key": public_key.encode(''),
                    }
                }
            ],
        }

        cloudiot_device = client.create_device(parient, device_template)
        device.cloudiot_device = cloudiot_device
        device.save()
