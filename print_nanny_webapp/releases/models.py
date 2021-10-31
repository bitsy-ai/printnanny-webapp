from django.db import models

from .choices import ReleaseChannel


class Release(models.Model):
    class Meta:
        ordering = ["-created_dt"]

    created_dt = models.DateTimeField(db_index=True, auto_now_add=True)
    ansible_extra_vars = models.JSONField()
    release_channel = models.CharField(
        max_length=8,
        choices=ReleaseChannel.choices,
        default=ReleaseChannel.STABLE,
    )
