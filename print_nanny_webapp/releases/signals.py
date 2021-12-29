import logging
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.conf import settings

logger = logging.getLogger(__name__)

User = get_user_model()
# when device is created, automatically create Task with type ACTIVATE_LICENSE
@receiver(post_save, sender=User, dispatch_uid="create_task_check_license")
def check_serviceuser_api_token(sender, instance, created, **kwargs):
    if instance.is_serviceuser:
        token = settings.SERVICEUSER_AUTH.get(instance.email)
        if token:
            logger.info(
                f"Using service token configured in Django settings for {instance.email}"
            )
            Token.objects.get_or_create(user=instance, key=token)
        else:
            logger.warning(
                f"Token for service user {instance.email} was not in Django settings. Generating new token."
            )
            Token.objects.get_or_create(
                user=instance,
            )
