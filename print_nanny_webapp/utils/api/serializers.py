from rest_framework import serializers
from django.conf import settings


class ErrorDetailSerializer(serializers.Serializer):
    detail = serializers.CharField()
    code = serializers.CharField()


class PrintNannyApiConfigSerializer(serializers.Serializer):
    bearer_access_token = serializers.CharField(read_only=True)
    base_path = serializers.CharField(read_only=True)
    static = serializers.SerializerMethodField(read_only=True)
    ws = serializers.SerializerMethodField(read_only=True)

    def get_static(self, _obj) -> str:
        absolute_url = self.request.build_absolute_uri(settings.WS_BASE_URL)
        return absolute_url

    def get_ws(self, _obj) -> str:
        return self.request.build_absolute_uri(settings.WS_BASE_URL)
