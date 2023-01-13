import os

from django.contrib.auth import get_user_model
from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from django.db.models import UniqueConstraint


User = get_user_model()


class MoonrakerServer(SafeDeleteModel):
    class Meta:
        index_together = (
            ("created_dt", "user", "pi", "updated_dt"),
            (
                "moonraker_version",
                "pip_version",
                "python_version",
                "pi",
            ),
        )
        constraints = [
            UniqueConstraint(
                fields=["pi"],
                condition=models.Q(deleted=None),
                name="unique_moonraker_server_per_pi",
            )
        ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="moonraker_servers"
    )
    pi = models.ForeignKey(
        "devices.Pi", on_delete=models.CASCADE, related_name="moonraker_servers"
    )
    moonraker_version = models.CharField(max_length=32, default="")
    pip_version = models.CharField(max_length=32, default="")
    python_version = models.CharField(max_length=32, default="")

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    api_key = models.CharField(max_length=255, null=True)

    @property
    def base_url(self) -> str:
        return self.pi.urls["moonraker_api"]

    @property
    def base_path(self) -> str:
        return "/home/printnanny/.moonraker/"

    @property
    def venv_path(self) -> str:
        return os.path.join(self.base_path, ".venv")

    @property
    def python_path(self) -> str:
        return os.path.join(self.venv_path, "bin/python")

    @property
    def pip_path(self) -> str:
        return os.path.join(self.venv_path, "bin/pip")
