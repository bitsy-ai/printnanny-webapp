import logging
from collections.abc import Mapping
from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer

from print_nanny_webapp.tasks.models import (
    Task,
    MonitorStartTask,
    MonitorStopTask,
    TaskStatus,
)
from print_nanny_webapp.tasks.enum import TaskStatusType, TaskType

logger = logging.getLogger(__name__)


class TaskSerializer(serializers.ModelSerializer):
    tasktype = serializers.ChoiceField(choices=TaskType.choices)

    class Meta:
        model = Task
        read_only_fields = ("user", "device", "created_dt")
        fields = "__all__"


class MonitorStartTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitorStartTask
        fields = "__all__"
        read_only_fields = ("device", "created_dt")

    def to_resource_type(self, _model_or_instance):
        return TaskType.CLOUD_MONITOR_START


class MonitorStopTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitorStopTask
        fields = "__all__"
        read_only_fields = ("device", "created_dt")

    def to_resource_type(self, _model_or_instance):
        return TaskType.CLOUD_MONITOR_STOP


class PolymorphicTaskSerializer(PolymorphicSerializer):
    resource_type_field_name = "model"
    model_serializer_mapping = {
        MonitorStartTask: MonitorStartTaskSerializer,
        MonitorStopTask: MonitorStopTaskSerializer,
    }

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
    task = PolymorphicTaskSerializer()

    class Meta:
        model = TaskStatus
        read_only_fields = ("task", "created_dt")
        fields = "__all__"
