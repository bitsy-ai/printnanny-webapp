from polymorphic.models import PolymorphicModel
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from django.contrib.auth import get_user_model
from django.db import models
from .enum import EventSource


UserModel = get_user_model()


class AbstractEvent(PolymorphicModel, SafeDeleteModel):
    """
    Polymorphic Base Event
    """

    class Meta:
        abstract = True
        ordering = ["-created_dt"]
        index_together = [["source", "subject", "created_dt"]]

    _safedelete_policy = SOFT_DELETE
    created_dt = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=32, choices=EventSource.choices)
    subject = models.CharField(max_length=255)
    payload = models.JSONField(default=dict)


class AbstractUserEvent(AbstractEvent):
    class Meta:
        abstract = True
        ordering = ["-created_dt"]
        index_together = [["user", "source", "subject", "created_dt"]]

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)


class AbstractPiEvent(AbstractEvent):
    class Meta:
        abstract = True
        ordering = ["-created_dt"]
        index_together = [["pi", "source", "subject", "created_dt"]]

    pi = models.ForeignKey("devices.Pi", on_delete=models.CASCADE)
