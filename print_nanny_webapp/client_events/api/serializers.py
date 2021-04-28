# from django.contrib.auth import get_user_model

# from rest_framework import serializers
# from rest_polymorphic.serializers import PolymorphicSerializer

# from print_nanny_webapp.client_events.models import (
#     ClientEvent,
#     OctoPrintEvent,
#     PrintSessionState,
#     PluginEvent,
# )


# class OctoPrintEventSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OctoPrintEvent
#         fields = [field.name for field in OctoPrintEvent._meta.fields] + ["url"]
#         extra_kwargs = {
#             "url": {"view_name": "api:octoprint-event-detail", "lookup_field": "id"}
#         }
#         read_only_fields = ("user",)


# class PluginEventSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PluginEvent
#         fields = [field.name for field in PluginEvent._meta.fields] + ["url"]
#         extra_kwargs = {
#             "url": {"view_name": "api:plugin-event-detail", "lookup_field": "id"}
#         }
#         read_only_fields = ("user",)


# class PrintSessionStateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PrintSessionState
#         fields = [field.name for field in PrintSessionState._meta.fields] + ["url"]
#         extra_kwargs = {
#             "url": {"view_name": "api:print-session-event-detail", "lookup_field": "id"}
#         }
#         read_only_fields = ("user",)
