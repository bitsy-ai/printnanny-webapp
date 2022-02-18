import logging
from collections.abc import Mapping
from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from rest_framework.fields import empty

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
        read_only_fields = ("device", "created_dt")
        fields = "__all__"


class JanusTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = JanusTask
        fields = "__all__"
        read_only_fields = ("device", "created_dt")


class PolymorphicTaskSerializer(PolymorphicSerializer):
    resource_type_field_name = "task_type"
    model_serializer_mapping = {JanusTask: JanusTaskSerializer}

    resourcetype_map = {
        JanusTaskType.CLOUD_MONITOR_START.value: JanusTask.__name__,
        JanusTaskType.CLOUD_MONITOR_STOP.value: JanusTask.__name__,
    }

    def create(self, validated_data):
        """
        Override PolymorphicSerializer.create to skip validated_data.pop(self.resource_type_field_name)
        """
        resource_type = validated_data[self.resource_type_field_name]
        serializer = self._get_serializer_from_resource_type(resource_type)
        return serializer.create(validated_data)

    def update(self, instance, validated_data):
        resource_type = validated_data[self.resource_type_field_name]
        serializer = self._get_serializer_from_resource_type(resource_type)
        return serializer.update(instance, validated_data)

    def _get_resource_type_from_mapping(self, mapping):
        logger.info(
            "PolymorphicEventSerializer mapping=%s resourcetype_map=%s",
            mapping,
            self.resourcetype_map,
        )
        try:
            task_type = mapping[self.resource_type_field_name]
            logger.info("PolymorphicEventSerializer task_type=%s", task_type)
            return self.resourcetype_map[task_type]
        except KeyError:
            raise serializers.ValidationError(
                {
                    self.resource_type_field_name: "Failed to extract resource from field",
                }
            )


class TaskStatusSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=TaskStatusType.choices)

    class Meta:
        model = TaskStatus
        read_only_fields = ("task", "created_dt")
        fields = "__all__"
