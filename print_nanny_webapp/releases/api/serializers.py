from rest_framework import serializers

from ..models import Release


class AnsibleExtraVarsSerializer(serializers.Serializer):
    janus_version = serializers.CharField()
    janus_libwebsockets_version = serializers.CharField()
    janus_libnice_version = serializers.CharField()
    janus_usrsctp_version = serializers.CharField()
    janus_libsrtp_version = serializers.CharField()

    tflite_version = serializers.CharField()
    printnanny_cli_version = serializers.CharField()
    libcamera_version = serializers.CharField()


class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = "__all__"
