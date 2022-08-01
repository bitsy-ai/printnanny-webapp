from django.contrib.auth import get_user_model
from django.db import models
from print_nanny_webapp.utils.fields import ChoiceArrayField

from .enum import AlertEventType
from .base import AbstractPiEvent, AbstractUserEvent

User = get_user_model()


class BaseAlertSettings(models.Model):
    class Meta:
        abstract = True

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enabled = models.BooleanField(default=True)
    event_types = ChoiceArrayField(
        models.CharField(choices=AlertEventType.choices, max_length=255),
        blank=True,
        default=list(
            [
                AlertEventType.PRINT_QUALITY,
                AlertEventType.PRINT_DONE,
                AlertEventType.PRINT_PROGRESS,
            ]
        ),
    )


class EmailAlertSettings(BaseAlertSettings):
    pass


class PrintJobAlert(AbstractPiEvent):
    """
    User-facing print job notification events
    """

    event_type = models.CharField(choices=AlertEventType.choices, max_length=32)
