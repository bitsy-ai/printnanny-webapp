from rest_framework import serializers

from print_nanny_webapp.crash_reports.models import CrashReport


class CrashReportSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj) -> str:
        return f"/crash-reports/{obj.id}/"

    class Meta:
        model = CrashReport
        exclude = ("deleted", "deleted_by_cascade")
        read_only_fields = ("id", "url", "user")
