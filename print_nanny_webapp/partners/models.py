import io
import os
from uuid import uuid4
from django.db import models
from django.utils import timezone, dateformat

from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE
from safedelete.managers import SafeDeleteManager
import qrcode

User = get_user_model()


def _upload_to(instance, filename):
    datesegment = dateformat.format(timezone.now(), "Y/M/d/")
    path = os.path.join(f"uploads/{instance.__class__.__name__}", datesegment, filename)
    return path


class GeeksToken(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["octoprint_device_id"],
                condition=models.Q(deleted=None),
                name="unique_geeks_token_per_octoprint_device",
            )
        ]

    # Grabbed code from rest_framework.models.Token
    key = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    octoprint_device = models.ForeignKey(
        "remote_control.OctoPrintDevice", null=True, on_delete=models.CASCADE
    )
    verified = models.BooleanField(default=False)
    qrcode = models.ImageField(upload_to=_upload_to)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.qrcode.name == "":
            output = io.BytesIO()
            img = qrcode.make(self.key)
            img.save(output, format="PNG")
            output.seek(0)
            self.qrcode.save(f"{self.key}.png", ContentFile(output.read()))

    def __str__(self):
        return self.key.hex
