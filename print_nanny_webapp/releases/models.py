from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from .choices import ReleaseChannel


class Release(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    class Meta:
        ordering = ["-created_dt"]

    created_dt = models.DateTimeField(db_index=True, auto_now_add=True)

    name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)

    manifest_url = models.CharField(max_length=255)

    sig_url = models.CharField(max_length=255)

    checksum = models.CharField(max_length=255)
    checksum_url = models.CharField(max_length=255)

    release_channel = models.CharField(
        max_length=8,
        choices=ReleaseChannel.choices,
        default=ReleaseChannel.STABLE,
    )
