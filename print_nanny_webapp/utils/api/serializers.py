from rest_framework import serializers


class ErrorDetailSerializer(serializers.Serializer):
    detail = serializers.CharField()


class PrintNannyApiConfigSerializer(serializers.Serializer):
    bearer_access_token = serializers.CharField(read_only=True)
    base_path = serializers.CharField(read_only=True)
