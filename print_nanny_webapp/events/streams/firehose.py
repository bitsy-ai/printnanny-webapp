import logging
import tempfile
import json
import asyncio

import nats
from channels.db import database_sync_to_async

import django
from django.conf import settings
from django.apps import apps

logger = logging.getLogger(__name__)

NATS_ROBOT_ACCOUNT_NAME = "firehose"

django.setup()
# settings.configure()
NatsRobotAccount = apps.get_model("django_nats_nkeys.NatsRobotAccount")
NatsRobotApp = apps.get_model("django_nats_nkeys.NatsRobotApp")


@database_sync_to_async
def get_robot_acccount():
    try:
        return NatsRobotAccount.objects.get(name=NATS_ROBOT_ACCOUNT_NAME)
    except NatsRobotAccount.DoesNotExist:
        return NatsRobotAccount.objects.create_nsc(name=NATS_ROBOT_ACCOUNT_NAME)


@database_sync_to_async
def get_robot_app(account):
    try:
        return NatsRobotApp.objects.get(
            app_name=NATS_ROBOT_ACCOUNT_NAME,
            account=account,
        )

    except NatsRobotApp.DoesNotExist:
        return NatsRobotApp.objects.create_nsc(
            app_name=NATS_ROBOT_ACCOUNT_NAME, account=account
        )


async def init_robot_app():
    account = await get_robot_acccount()
    app = await get_robot_app(account)

    return app


@database_sync_to_async
def handle_pi_event(msg):
    subject = msg.subject
    reply = msg.reply
    data = json.loads(msg.data.decode("utf-8"))
    logger.debug(
        "Received NATS msg subject=%s reply=%s: data=%s",
        subject=subject,
        reply=reply,
        data=data,
    )
    from print_nanny_webapp.events.api.serializers import PolymorphicPiEventSerializer

    serializer = PolymorphicPiEventSerializer(data=data)
    if serializer.is_valid():
        obj = serializer.save()
        logger.info("Saved obj %s", obj)
    else:
        logger.error("Error serializing event %s", serializer.errors)


@database_sync_to_async
def get_creds(app):
    from django_nats_nkeys.services import nsc_generate_creds, nsc_push

    creds = nsc_generate_creds(app.account.name, app_name=app.app_name)
    nsc_push()
    return creds


async def main():

    app = await init_robot_app()

    logger.info(
        "Initializing worker subscribed to %s using app identity %s",
        NATS_ROBOT_ACCOUNT_NAME,
        app,
    )

    nats_creds = await get_creds(app)

    with tempfile.NamedTemporaryFile() as f:
        f.write(nats_creds.encode("utf-8"))
        f.flush()
        logger.info("Wrote credentials to %s", f.name)
        nc = await nats.connect(
            settings.NATS_SERVER_URI,
            user_credentials=f.name,
            allow_reconnect=True,
            verbose=True,
        )

        logger.info("Initialized Nats connection to %s", settings.NATS_SERVER_URI)

        sub = await nc.subscribe("pi.>")

        logger.info("Subscribed to pi.>")

        async for msg in sub.messages:
            await handle_pi_event(msg)


if __name__ == "__main__":
    asyncio.run(main())
