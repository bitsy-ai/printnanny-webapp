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
    result = NatsRobotAccount.objects.get(name=NATS_ROBOT_ACCOUNT_NAME)
    logger.info("Fetched NatsRobotAccount with id=%s name=%s", result.id, result.name)
    return result


@database_sync_to_async
def get_robot_app(account):
    app = NatsRobotApp.objects.get(
        app_name=NATS_ROBOT_ACCOUNT_NAME,
        account=account,
    )
    logger.info("Fetched NatsRobotApp id=%s name=%s", app.id, app.name)
    return app


async def init_robot_app():
    try:
        account = await get_robot_acccount()
        app = await get_robot_app(account)
        return app
    except NatsRobotAccount.DoesNotExist:
        logger.error(
            "NatsRobotAccount.DoesNotExist %s",
            NATS_ROBOT_ACCOUNT_NAME,
        )
        return
    except NatsRobotApp.DoesNotExist:
        logger.error(
            "NatsRobotApp.DoesNotExist %s",
            NATS_ROBOT_ACCOUNT_NAME,
        )
        return


@database_sync_to_async
def handle_pi_event(msg):
    data = json.loads(msg.data.decode("utf-8"))
    logger.info(
        "Received NATS msg %s",
        msg,
    )
    from print_nanny_webapp.events.api.serializers import PolymorphicPiEventSerializer

    serializer = PolymorphicPiEventSerializer(data=data)
    if serializer.is_valid():
        obj = serializer.save()
        logger.info("Saved obj %s", obj)
    else:
        logger.error("Error serializing event %s", serializer.errors)


async def main():
    from django_nats_nkeys.services import nsc_pull
    from django_nats_nkeys.services import nsc_generate_creds

    app = await init_robot_app()

    if app is None:
        logger.error("Failed to get NatsRobotApp, exiting")
        exit(1)

    nsc_pull(force=True)
    logger.info(
        "Initializing worker subscribed to %s using app identity %s",
        NATS_ROBOT_ACCOUNT_NAME,
        app,
    )

    nats_creds = nsc_generate_creds(app.account.name, app_name=app.app_name)
    logger.info("Generated NKEY credential for app=%s", NATS_ROBOT_ACCOUNT_NAME)

    with tempfile.NamedTemporaryFile() as f:
        logger.info("Attempting to write NKEY credential to %s", f.name)
        f.write(nats_creds.encode("utf-8"))
        f.flush()
        logger.info("Success! Wrote NKEY credential to %s", f.name)
        logger.info("Attempting to connect to NATS server %s", settings.NATS_SERVER_URI)
        nc = await nats.connect(
            settings.NATS_SERVER_URI,
            user_credentials=f.name,
            allow_reconnect=True,
            verbose=True,
        )

        logger.info(
            "Success! Initialized Nats connection to %s", settings.NATS_SERVER_URI
        )
        sub = await nc.subscribe("pi.>")

        logger.info("Subscribed to pi.>")

        async for msg in sub.messages:
            await handle_pi_event(msg)


if __name__ == "__main__":
    logger.info("Initializing firehose event app")
    asyncio.run(main())
