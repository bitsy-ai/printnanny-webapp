import logging
import io
import zipfile
from uuid import uuid4
from typing import Tuple, Dict, Any
from datetime import timedelta
import requests

from django.utils import timezone
from django.http import HttpRequest
from django.conf import settings
from django.db.models import Q
from django.template.loader import render_to_string
from django_nats_nkeys.models import (
    NatsMessageExport,
    NatsMessageExportType,
    NatsRobotAccount,
    NatsOrganizationUser,
    _default_name,
)
from django_nats_nkeys.services import create_organization, nsc_generate_creds
from print_nanny_webapp.utils.api.service import get_api_config
from print_nanny_webapp.devices.enum import JanusConfigType
from print_nanny_webapp.devices.api.serializers import PrintNannyLicenseSerializer
from print_nanny_webapp.devices.models import (
    Pi,
    PiNatsApp,
    WebrtcStream,
)

logger = logging.getLogger(__name__)


class StreamingMountpointNotFound(Exception):
    pass


def janus_stream_clean(max_age_seconds: int = 3600):
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

    streaming_list = res.json().get("plugindata", {}).get("data", {}).get("list", [])

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
            if td.seconds > max_age_seconds:  # 1 hour
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


def janus_cloud_admin_add_token(token: str) -> Dict[str, Any]:
    req = dict(
        janus="add_token",
        token=token,
        admin_secret=settings.JANUS_CLOUD_ADMIN_SECRET,
        plugins=["janus.plugin.streaming"],
        transaction=uuid4().hex,
    )
    res = requests.post(settings.JANUS_CLOUD_ADMIN_URL, json=req)
    logger.info("Got response to POST %s: %s", settings.JANUS_CLOUD_ADMIN_URL, res)
    res.raise_for_status()
    return res.json()


def janus_get_session(api_url: str, token: str) -> str:
    req = dict(
        transaction=str(uuid4()),
        janus="create",
        admin_secret=settings.JANUS_CLOUD_ADMIN_SECRET,
        token=token,
    )
    res = requests.post(api_url, json=req)
    res.raise_for_status()
    data = res.json()
    logger.info("Created Janus session %s", data)
    return data["data"]["id"]


def janus_get_plugin_handle(api_url: str, session: str, token) -> str:
    req = dict(
        transaction=str(uuid4()),
        janus="attach",
        plugin="janus.plugin.streaming",
        admin_secret=settings.JANUS_CLOUD_ADMIN_SECRET,
        token=token,
    )
    endpoint = f"{api_url}/{session}"
    res = requests.post(endpoint, json=req)
    res.raise_for_status()
    data = res.json()
    logger.info("Attached plugin handle %s", data)
    return data["data"]["id"]


def janus_get_streaming_info(
    stream: WebrtcStream, handle_endpoint: str
) -> Dict[str, Any]:
    data = dict(
        transaction=str(uuid4()),
        janus="message",
        token=stream.api_token,
        admin_secret=settings.JANUS_CLOUD_ADMIN_SECRET,
        body=dict(
            request="info",
            id=stream.id,
            secret=stream.stream_secret,
        ),
    )
    res = requests.post(handle_endpoint, json=data)
    res.raise_for_status()
    res_data = res.json()
    logger.info("Got streaming info %s", res_data)
    error_code = res_data.get("plugindata", {}).get("data", {}).get("error_code")
    if error_code == 455:
        error = res_data.get("plugindata", {}).get("data", {}).get("error")
        raise StreamingMountpointNotFound(error)
    return res_data.get("plugindata", res_data)


def janus_create_streaming_mountpoint(
    stream: WebrtcStream, handle_endpoint: str
) -> Dict[str, Any]:
    admin_key = (
        settings.JANUS_CLOUD_STREAMING_PLUGIN_ADMIN_KEY
        if stream.config_type == JanusConfigType.CLOUD
        else stream.admin_secret
    )
    media = [
        dict(
            type="video",
            mid="video0",
            label="H264-encoded camera stream",
            pt=stream.pt,
            rtpmap=stream.rtpmap,
            port=stream.video_rtp_port,
            bufferkf=True,
        ),
        dict(
            type="data",
            mid="tensor0",
            label="Bytestream of tensor data",
            buffermsg=True,
            port=stream.data_rtp_port,
        ),
    ]
    data = dict(
        transaction=str(uuid4()),
        janus="message",
        token=stream.api_token,
        admin_secret=settings.JANUS_CLOUD_ADMIN_SECRET,
        body=dict(
            request="create",
            admin_key=admin_key,
            type="rtp",
            id=stream.id,
            description=f"WebRTC stream config_type={stream.config_type} pi={stream.pi.id}",
            secret=stream.stream_secret,
            pin=stream.stream_pin,
            is_private=False,  # stream is still private (pin and token protected) - this setting controls whether or not steam is visible in LIST view
            permanent=False,
            media=media,
        ),
    )
    res = requests.post(handle_endpoint, json=data)
    res.raise_for_status()
    res_data = res.json()
    logger.info(
        "%s response to 'create' streaming mountpoint: %s ", handle_endpoint, res_data
    )
    return janus_get_streaming_info(stream, handle_endpoint)


def janus_streaming_get_or_create_mountpoint(stream: WebrtcStream):
    janus_cloud_admin_add_token(stream.api_token)
    session = janus_get_session(stream.api_url, stream.api_token)
    plugin_handle = janus_get_plugin_handle(stream.api_url, session, stream.api_token)
    handle_endpoint = stream.plugin_handle_endpoint(session, plugin_handle)

    try:
        streaming_info = janus_get_streaming_info(stream, handle_endpoint)
    except StreamingMountpointNotFound:
        streaming_info = janus_create_streaming_mountpoint(stream, handle_endpoint)

    stream.info = streaming_info
    stream.save()
    return stream


def render_janus_env(device: Pi) -> str:
    context = dict(
        janus_admin_secret=device.active_license.janus_admin_secret,
        janus_token=device.active_license.janus_token,
    )
    return render_to_string("janus.env.j2", context)


def render_honeycomb_env() -> str:
    context = dict(
        honeycomb_dataset=settings.HONEYCOMB_DATASET,
        honeycomb_api_key=settings.HONEYCOMB_API_KEY,
    )
    return render_to_string("honeycomb.env.j2", context)


def janus_cloud_setup(device: Pi) -> Tuple[WebrtcStream, bool]:
    # 1) get or create WebrtcStream mountpoint
    stream, created = WebrtcStream.objects.get_or_create(
        device=device, config_type=JanusConfigType.CLOUD
    )
    logger.info(
        "Retrieved WebrtcStream id=%s user=%s created=%s",
        stream.id,
        device.user.id,
        created,
    )

    # 2) ensure token added to Janus Gateway
    # Janus stores tokens in memory, so added tokens are flushed on restart
    logger.info("Retrieved WebrtcStream %s created=%s", stream, created)
    return stream, created


def get_or_create_import_export_streams(app: PiNatsApp) -> None:
    """
    By default, NATS messages are scoped to an account (represented by a Django organization by django-nats-nkeys)

    To allow our alerts/database services to subscribe to messages, we must export a stream that is imported by a NatsRobotAccount
    """
    # try getting NatsMessageExport app subject pattern
    try:
        nats_export = NatsMessageExport.objects.get(
            name=app.app_name,
            subject_pattern=app.nats_subject_pattern,
        )
        logger.info("Found NatsMessageExport %s", nats_export)
    except NatsMessageExport.DoesNotExist:
        # create export for this app
        nats_export = NatsMessageExport.objects.create(
            name=app.app_name,
            subject_pattern=app.nats_subject_pattern,
            export_type=NatsMessageExportType.STREAM,
            public=False,
        )
        logger.info("Created NatsMessageExport %s", nats_export)
    # first, create an interested importer entry
    for robot_account in NatsRobotAccount.objects.all():
        robot_account.imports.add(nats_export)
        robot_account.save()
        logger.info(
            "Added NatsMessageExport %s to NatsRobotAccount.exports %s",
            nats_export,
            robot_account,
        )
    # after importers have been configred, add exporter relationship. nsc commands are handled in django_nats_nkeys.signals.add_nats_organization_export
    app.organization.exports.add(nats_export)
    app.organization.save()
    logger.info(
        "Added NatsMessageExport %s to NatsOrganization.imports %s",
        nats_export,
        app.organization,
    )


def get_or_create_pi_nats_app(pi: Pi) -> PiNatsApp:
    # get or create organization associated with Pi.user
    try:
        org_user = NatsOrganizationUser.objects.get(user=pi.user)
    except NatsOrganizationUser.DoesNotExist:
        create_organization(
            pi.user,
            _default_name(),
            org_user_defaults={"is_admin": True},
        )
        org_user = NatsOrganizationUser.objects.get(user=pi.user)

    # is there a NATS app already associated with this Pi?
    try:
        app = PiNatsApp.objects.get(pi=pi)
        # handle app in potentially half-created state
        validator = app.nsc_validate()
        if validator.ok() is False:
            raise Exception(f"PiNatsApp validation failed {validator.result.stdout}")

    # create nats app associated with org user
    except PiNatsApp.DoesNotExist:
        app = PiNatsApp.objects.create_nsc(
            app_name=_default_name(),
            organization_user=org_user,
            organization=org_user.organization,
            pi=pi,
        )
    get_or_create_import_export_streams(app)

    return app


def get_license_serializer(pi: Pi, request: HttpRequest) -> PrintNannyLicenseSerializer:
    api = get_api_config(request, user=pi.user)
    return PrintNannyLicenseSerializer(dict(api=api, pi=pi))


def build_license_zip(pi: Pi) -> bytes:
    nats_app = get_or_create_pi_nats_app(pi)
    nats_creds = nsc_generate_creds(
        nats_app.organization.name, app_name=nats_app.app_name
    )
    creds_bundle = [
        ("printnanny-cloud-nats.creds", nats_creds),
    ]

    # do not write sensitive credentials to disk
    # instead, write to memory buffer
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a") as zip_obj:
        for file_name, data in creds_bundle:
            zip_obj.writestr(file_name, data)
    return zip_buffer.getvalue()
