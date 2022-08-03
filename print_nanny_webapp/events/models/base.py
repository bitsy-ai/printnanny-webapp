from polymorphic.models import PolymorphicModel
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from django.contrib.auth import get_user_model
from django.db import models
from .enum import EventSource


User = get_user_model()


class AbstractEvent(PolymorphicModel, SafeDeleteModel):
    """
    Polymorphic Base Event
    """

    class Meta:
        abstract = True
        ordering = ["-created_dt"]
        index_together = [["subject", "created_dt"]]

    _safedelete_policy = SOFT_DELETE
    created_dt = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=255)
    payload = models.JSONField(default=dict)


class AbstractUserEvent(AbstractEvent):
    class Meta:
        abstract = True
        ordering = ["-created_dt"]
        index_together = [["user", "subject", "created_dt"]]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # type: ignore[var-annotated]


class AbstractPiEvent(AbstractEvent):
    class Meta:
        abstract = True
        ordering = ["-created_dt"]
        index_together = [["pi", "subject", "created_dt"]]

    pi = models.ForeignKey("devices.Pi", on_delete=models.CASCADE)
