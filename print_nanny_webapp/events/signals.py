# import logging
# # from typing import Callable, Dict, Tuple, Any
# from asgiref.sync import sync_to_async

# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from .models import BasePiEvent
# from .api.serializers import PolymorphicPiEventSerializer
# from print_nanny_webapp.devices.models import PiNatsApp
# from django_nats_nkeys.services import nsc_generate_creds
# # from print_nanny_webapp.events.models import Event
# # from .services import (
# #     broadcast_event,
# #     webrtc_stream_start,
# #     webrtc_stream_stop,
# # )
# # from .models.enum import WebRTCEventName, WebRTCCommandName

# logger = logging.getLogger(__name__)

# # created_handlers: Dict[str, Callable[..., Any]] = {
# #     WebRTCCommandName.STREAM_START.value: webrtc_stream_start,
# #     WebRTCCommandName.STREAM_STOP.value: webrtc_stream_stop,
# #     WebRTCEventName.STREAM_START_ERROR.value: broadcast_event,
# #     WebRTCEventName.STREAM_START_SUCCESS.value: broadcast_event,
# # }


# @receiver(post_save, sender=BasePiEvent, dispatch_uid="event_save_handler")
# def handle_event(sender, instance, created, **kwargs):
#     if created is True:
#         logger.debug(
#             "events.signals.handle_event calling handler %s with instance %s model %s",
#             instance,
#             instance.model,
#         )
#         nats_app = PiNatsApp.objects.get(pi=instance.pi)
#         creds = nsc_generate_creds(nats_app.organization, nats_app)

#         nc =
