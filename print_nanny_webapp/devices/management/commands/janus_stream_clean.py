from datetime import timedelta
import logging
from uuid import uuid4
import requests
from django.core.management.base import BaseCommand
from django.db.models import Q
from django.conf import settings
from django.utils import timezone

from print_nanny_webapp.devices.enum import JanusConfigType

from print_nanny_webapp.devices.models import WebrtcStream
from print_nanny_webapp.devices.services import (
    janus_cloud_admin_add_token,
    janus_get_plugin_handle,
    janus_get_session,
)

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Destroys Janus stream mountpoints with 0 users and de-allocates UDP ports"

    def add_arguments(self, parser):
        parser.add_argument("--email", type=str)
        parser.add_argument("--hostname", type=str)
        parser.add_argument("--out", type=str)
        parser.add_argument("--port", type=int, default=8000)

    def handle(self, *args, **options):

        active_cloud_webrtc_streams = WebrtcStream.objects.filter(
            ~Q(video_rtp_port=None, data_rtp_port=None),
            config_type=JanusConfigType,
        ).all()

        logger.warning(
            "Found %s cloud WebrtcStreams with port allocations, scanning for inactive streams",
            active_cloud_webrtc_streams.count(),
        )
        token = str(uuid4())
        janus_cloud_admin_add_token(token)

        session = janus_get_session(settings.JANUS_CLOUD_API_URL, token)

        plugin_handle = janus_get_plugin_handle(
            settings.JANUS_CLOUD_API_URL, session, token
        )

        handle_endpoint = f"{settings.JANUS_CLOUD_API_URL}/{session}/{plugin_handle}"
        logger.warning("Initialized plugin handle %s", handle_endpoint)
        # for stream in active_cloud_webrtc_streams:

        # list janus streaming mountpoints
        req = dict(
            transaction=str(uuid4()),
            janus="message",
            admin_secret=settings.JANUS_CLOUD_ADMIN_SECRET,
            token=token,
            body=dict(request="list"),
        )
        res = requests.post(handle_endpoint, json=req)

        # janus returns a 200 response with error code in the body (ugh), so handle that
        if res.json().get("error") is not None:
            logger.error(
                "Janus Gateway responded with error to streaming list request %s", res
            )
            return

        streaming_list = (
            res.json().get("plugindata", {}).get("data", {}).get("list", [])
        )

        logger.warning(
            "Analyzing %s Janus Gateway streaming mountpoints for active viewers",
            streaming_list,
        )

        for stream in streaming_list:
            # number of viewers requires a separate info request
            stream_id = stream.get("id")
            if stream_id is None:
                logger.warning("Failed to parse stream id from %s", stream)
                continue
            webrtc_stream_model = WebrtcStream.objects.get(
                config_type=JanusConfigType.CLOUD, id=stream_id
            )
            req = dict(
                transaction=str(uuid4()),
                janus="message",
                admin_secret=settings.JANUS_CLOUD_ADMIN_SECRET,
                token=token,
                body=dict(
                    request="info",
                    id=stream_id,
                    secret=webrtc_stream_model.stream_secret,
                ),
            )

            res = requests.post(handle_endpoint, json=req)
            # janus returns a 200 response with error code in the body (ugh), so handle that
            if res.json().get("error") is not None:
                logger.error(
                    "Janus Gateway responded with error to streaming info request %s",
                    res,
                )
                continue

            # if the stream has 0 viewers and hasn't been updated within the last hour, reclaim ports
            logger.info("Stream info %s", res.json())
            viewers = (
                res.json()
                .get("plugindata", {})
                .get("data", {})
                .get("info", {})
                .get("viewers", 0)
            )  # .get("info", {})
            logger.info("Stream %s has %s viewers", stream_id, viewers)
            if viewers == 0:
                webrtc_stream_model = WebrtcStream.objects.get(
                    config_type=JanusConfigType.CLOUD, id=stream_id
                )
                now = timezone.now()
                td: timedelta = now - webrtc_stream_model.updated_dt
                logger.info("Stream last updated %s ( %s seconds ago)", td, td.seconds)
                if td.seconds > 3600:  # 1 hour
                    logger.warning(
                        "Stream %s has no viewers and was lasted updated %s ago. Destroying mountpoint.",
                        stream_id,
                        td,
                    )
                    # destroy the stream mountpoint
                    req = dict(
                        transaction=str(uuid4()),
                        janus="message",
                        admin_secret=settings.JANUS_CLOUD_ADMIN_SECRET,
                        token=token,
                        body=dict(request="destroy", id=stream_id),
                    )
                    res = requests.post(handle_endpoint, json=req)
                    # janus returns a 200 response with error code in the body (ugh), so handle that
                    if res.json().get("error") is not None:
                        logger.error(
                            "Janus Gateway responded with error to streaming info request %s",
                            res,
                        )

                    # unset video/data rtp ports
                    webrtc_stream_model.video_rtp_port = None
                    webrtc_stream_model.data_rtp_port = None
                    webrtc_stream_model.save()
                    logger.warning(
                        "Finished reclaiming ports from WebRtc stream %s",
                        webrtc_stream_model,
                    )
