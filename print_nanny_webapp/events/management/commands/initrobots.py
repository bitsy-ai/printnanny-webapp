import logging
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.apps import apps
from django_nats_nkeys.services import nsc_push

logger = logging.getLogger(__name__)
User = get_user_model()

NatsRobotAccount = apps.get_model("django_nats_nkeys.NatsRobotAccount")
NatsRobotApp = apps.get_model("django_nats_nkeys.NatsRobotApp")


def get_robot_acccount(name):
    try:
        result = NatsRobotAccount.objects.get(name=name)
        logger.info("Found existing NatsRobotAccount %s", result.__dict__)
    except NatsRobotAccount.DoesNotExist:
        result = NatsRobotAccount.objects.create_nsc(name=name)
        logger.info("Created new NatsRobotAccount %s", result.__dict__)
    return result


def get_robot_app(account, app_name):
    try:
        result = NatsRobotApp.objects.get(
            app_name=app_name,
            account=account,
        )
        logger.info("Found existing NatsRobotApp %s", result.__dict__)

    except NatsRobotApp.DoesNotExist:
        result = NatsRobotApp.objects.create_nsc(app_name=app_name, account=account)
        logger.info("Created new NatsRobotApp %s", result.__dict__)

    return result


class Command(BaseCommand):
    help = "Initializes a robot account/app (indempotent)"

    def add_arguments(self, parser):
        parser.add_argument("--name", type=str, default="firehose")

    def handle(self, *args, **kwargs):
        name = kwargs.get("name")
        account = get_robot_acccount(name)
        app = get_robot_app(account, name)
        nsc_push()

        logger.info("NatsRobotApp initialized %s", app.json)
