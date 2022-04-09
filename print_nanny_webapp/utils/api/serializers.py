from rest_framework import serializers


class ErrorDetailSerializer(serializers.Serializer):
    detail = serializers.CharField()
    code = serializers.CharField()


class PrintNannyApiConfigSerializer(serializers.Serializer):
    bearer_access_token = serializers.CharField(
        read_only=True, required=False, allow_null=True
    )
    base_path = serializers.CharField(read_only=True)
    static_url = serializers.CharField(read_only=True)
    dashboard_url = serializers.CharField(read_only=True)
