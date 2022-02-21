import json
from rest_framework import serializers
from rest_framework.renderers import JSONOpenAPIRenderer


class ErrorDetailSerializer(serializers.Serializer):
    detail = serializers.CharField()
    code = serializers.CharField()


class PrintNannyApiConfigSerializer(serializers.Serializer):
    bearer_access_token = serializers.CharField(read_only=True)
    base_path = serializers.CharField(read_only=True)


class JSONWebSocketRenderer(JSONOpenAPIRenderer):
    """
    Return json.dumps representation
    """

    def render(self, data, media_type=None, renderer_context=None):
        return json.dumps(
            data, cls=self.encoder_class, indent=2, ensure_ascii=self.ensure_ascii
        )
