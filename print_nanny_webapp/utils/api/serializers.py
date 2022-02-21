import json
from rest_framework import serializers
from rest_framework.renderers import JSONOpenAPIRenderer


class ErrorDetailSerializer(serializers.Serializer):
    detail = serializers.CharField()
    code = serializers.CharField()


class PrintNannyApiConfigSerializer(serializers.Serializer):
    bearer_access_token = serializers.CharField(read_only=True)
    base_path = serializers.CharField(read_only=True)
