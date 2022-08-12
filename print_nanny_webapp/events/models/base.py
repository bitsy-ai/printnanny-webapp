import uuid
from polymorphic.models import PolymorphicModel
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class AbstractEvent(PolymorphicModel, SafeDeleteModel):
    """
    Polymorphic Base Event
    """

    class Meta:
        abstract = True
        ordering = ["-created_dt"]
        index_together = [["id", "created_dt"]]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    _safedelete_policy = SOFT_DELETE
    created_dt = models.DateTimeField(auto_now_add=True)
    payload = models.JSONField(null=True)


class AbstractUserEvent(AbstractEvent):
    subject_pattern = "user.{user_id}"

    class Meta:
        abstract = True
        ordering = ["-created_dt"]
        index_together = [["id", "user", "created_dt"]]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # type: ignore[var-annotated]

    @property
    def subject(self):
        return self.subject_pattern.format(user_id=self.user.id)


class AbstractPiEvent(AbstractEvent):
    subject_pattern = "pi.{pi_id}"

    class Meta:
        abstract = True
        ordering = ["-created_dt"]
        index_together = [["id", "pi", "created_dt"]]

    pi = models.ForeignKey("devices.Pi", on_delete=models.CASCADE)

    @property
    def subject(self):
        return self.subject_pattern.format(pi_id=self.pi.id)
