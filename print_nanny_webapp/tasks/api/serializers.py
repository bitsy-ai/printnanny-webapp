import logging
from collections.abc import Mapping
from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer

from print_nanny_webapp.tasks.models import (
    JanusTask,
    Task,
    TaskStatus,
)
from print_nanny_webapp.tasks.enum import TaskStatusType, JanusTaskType

logger = logging.getLogger(__name__)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        read_only_fields = ("user", "device", "created_dt")
        fields = "__all__"


class JanusTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = JanusTask
        fields = "__all__"
        read_only_fields = ("device", "created_dt", "stream_config")


class PolymorphicTaskSerializer(PolymorphicSerializer):
    resource_type_field_name = "task_type"
    model_serializer_mapping = {JanusTask: JanusTaskSerializer}

    resourcetype_map = {
        JanusTaskType.CLOUD_MONITOR_START: JanusTask,
        JanusTaskType.CLOUD_MONITOR_STOP: JanusTask,
    }

    def _get_resource_type_from_mapping(self, mapping):
        logger.debug(
            "Got PolymorphicEventSerializer mapping=%s resourcetype_map=%s",
            mapping,
            self.resourcetype_map,
        )
        try:
            model = self.resourcetype_map[self.resource_type_field_name]
            return mapping[model]
        except KeyError:
            raise serializers.ValidationError(
                {
                    self.resource_type_field_name: "This field is required",
                }
            )

    def to_representation(self, instance):
        if isinstance(instance, Mapping):
            resource_type = self._get_resource_type_from_mapping(instance)
            serializer = self._get_serializer_from_resource_type(resource_type)
        else:
            resource_type = self.to_resource_type(instance)
            serializer = self._get_serializer_from_model_or_instance(instance)

        ret = serializer.to_representation(instance)
        return ret


class TaskStatusSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=TaskStatusType.choices)

    class Meta:
        model = TaskStatus
        read_only_fields = ("task", "created_dt")
        fields = "__all__"
