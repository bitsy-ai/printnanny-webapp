import logging
import io
import zipfile
from uuid import uuid4
from typing import Tuple, Dict, Any

import requests
from django.http import HttpRequest
from django.conf import settings
from django.template.loader import render_to_string
from django_nats_nkeys.models import (
    NatsMessageExport,
    NatsMessageExportType,
    NatsRobotAccount,
    NatsRobotApp,
    NatsOrganizationUser,
    _default_name,
)
from django_nats_nkeys.services import create_organization, nsc_generate_creds
from rest_framework.renderers import JSONRenderer
from print_nanny_webapp.utils.api.service import get_api_config
from print_nanny_webapp.devices.enum import JanusConfigType
from print_nanny_webapp.devices.api.serializers import PrintNannyLicenseSerializer
from print_nanny_webapp.devices.models import (
    Pi,
    PiNatsApp,
    WebrtcStream,
)

logger = logging.getLogger(__name__)


def init_robots():
    NATS_ROBOT_ACCOUNT_DB_WRITER_NAME = "firehose"

    try:
        NATS_ROBOT_DB_WRITER_ACCOUNT = NatsRobotAccount.objects.get(
            name=NATS_ROBOT_ACCOUNT_DB_WRITER_NAME
        )
    except NatsRobotAccount.DoesNotExist:
        NATS_ROBOT_DB_WRITER_ACCOUNT = NatsRobotAccount.objects.create_nsc(
            name=NATS_ROBOT_ACCOUNT_DB_WRITER_NAME
        )

    try:
        NatsRobotApp.objects.get(
            app_name=NATS_ROBOT_ACCOUNT_DB_WRITER_NAME,
            account=NATS_ROBOT_DB_WRITER_ACCOUNT,
        )

    except NatsRobotApp.DoesNotExist:
        NATS_ROBOT_APP_DB_WRITER = NatsRobotApp.objects.create_nsc(
            app_name=NATS_ROBOT_ACCOUNT_DB_WRITER_NAME,
            account=NATS_ROBOT_DB_WRITER_ACCOUNT,
        )


def janus_admin_add_token(stream: WebrtcStream) -> Dict[str, Any]:
    if stream.config_type == JanusConfigType.CLOUD:
        req = dict(
            janus="add_token",
            token=stream.api_token,
            admin_secret=settings.JANUS_CLOUD_ADMIN_SECRET,
            plugins=["janus.plugin.streaming"],
            transaction=uuid4().hex,
        )
        res = requests.post(stream.admin_url, json=req)
        logger.info("Got response to POST %s: %s", stream.admin_url, res)
        res.raise_for_status()
        return res.json()
    else:
        raise NotImplementedError(
            f"janus_admin_add_token not implemented in events.services for JanusConfigType={JanusConfigType.EDGE}"
        )


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
    # janus_admin_add_token(janus_auth)
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


def get_license_serializer(
    pi: Pi, nats_app: PiNatsApp, request: HttpRequest
) -> PrintNannyLicenseSerializer:
    api = get_api_config(request, user=pi.user)
    return PrintNannyLicenseSerializer(dict(api=api, nats_app=nats_app, pi=pi))


def build_license_zip(pi: Pi, request: HttpRequest) -> bytes:

    nats_app = get_or_create_pi_nats_app(pi)

    license_serializer = get_license_serializer(pi, nats_app, request)

    nats_creds = nsc_generate_creds(
        nats_app.organization.name, app_name=nats_app.app_name
    )

    creds_bundle = [
        ("license.json", JSONRenderer().render(license_serializer.data)),
        ("nats.creds", nats_creds),
    ]

    # do not write sensitive credentials to disk
    # instead, write to memory buffer
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a") as zip_obj:
        for file_name, data in creds_bundle:
            zip_obj.writestr(file_name, data)
    return zip_buffer.getvalue()
