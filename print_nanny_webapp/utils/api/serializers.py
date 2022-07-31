import copy
from collections import OrderedDict

from rest_framework import serializers
from rest_framework.utils import model_meta


class ErrorDetailSerializer(serializers.Serializer):
    detail = serializers.CharField()
    code = serializers.CharField()


class PrintNannyApiConfigSerializer(serializers.Serializer):
    bearer_access_token = serializers.CharField(
        read_only=True, required=False, allow_null=True
    )
    base_path = serializers.CharField(read_only=True)


class OptionsMetadataSerializer(serializers.Serializer):
    """
    An `OptionsModelSerializer` documents the OPTIONS response for a model endpoint
    """

    name = serializers.CharField()
    description = serializers.CharField()
    renders = serializers.ListField(child=serializers.CharField())
    parses = serializers.ListField(child=serializers.CharField())
    fieldset = serializers.DictField()
