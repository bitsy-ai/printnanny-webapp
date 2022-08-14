import tempfile
import logging
from asgiref.sync import async_to_sync
from django_nats_nkeys.services import nsc_generate_creds
from django.conf import settings
from rest_framework.renderers import JSONRenderer
import nats

from print_nanny_webapp.devices.models import PiNatsApp
from print_nanny_webapp.events.api.serializers import PolymorphicPiEventSerializer
from print_nanny_webapp.events.models.pi import BasePiEvent


logger = logging.getLogger(__name__)


def nats_publish(serializer: PolymorphicPiEventSerializer, obj: BasePiEvent):
    nats_app = PiNatsApp.objects.get(pi=obj.pi)
    creds = nsc_generate_creds(nats_app.organization.name, app_name=nats_app)
    with tempfile.NamedTemporaryFile() as f:
        f.write(creds.encode("utf-8"))
        f.flush()
        nc_sync = async_to_sync(nats.connect)
        nc_client = nc_sync(
            settings.NATS_SERVER_URI,
            user_credentials=f.name,
            allow_reconnect=False,
            verbose=True,
        )
        sync_publish = async_to_sync(nc_client.publish)
        sync_publish(obj.subject, JSONRenderer().render(serializer.data))
        logger.info("NATS published %s %s", obj.event_type, obj.subject)
