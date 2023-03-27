import logging
from typing import Dict, Any, Tuple
from rest_framework import serializers

from print_nanny_webapp.moonraker.models import MoonrakerServer

logger = logging.getLogger(__name__)


class MoonrakerServerSerializer(serializers.ModelSerializer):
    base_url = serializers.CharField(read_only=True)
    base_path = serializers.CharField()
    venv_path = serializers.CharField(read_only=True)
    pip_path = serializers.CharField(read_only=True)
    python_path = serializers.CharField(read_only=True)

    class Meta:
        model = MoonrakerServer
        exclude = ("deleted", "deleted_by_cascade")
        read_only_fields = ("user", "base_path", "base_url")

    def update_or_create(
        self, validated_data: Dict[Any, Any], device_id: int, user_id: int
    ) -> Tuple[MoonrakerServer, bool]:
        instance, created = MoonrakerServer.objects.filter(
            pi=device_id, user=user_id
        ).update_or_create(pi=device_id, user=user_id, defaults=validated_data)
        logger.info("Saved %s created=%s", instance, created)

        return instance, created
