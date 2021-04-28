from enum import unique
from print_nanny_webapp.utils import fields
from print_nanny_webapp.partners.models import GeeksToken
from django.forms import ModelForm
from django.forms import modelformset_factory
from .models import (
    AlertSettings,
    RemoteControlCommandAlertSettings,
    DiscordMethodSettings,
)



class AlertSettingsForm(ModelForm):
    class Meta:
        model = AlertSettings
        fields = ("event_types", "print_process_percent")


# class CommandAlertSettingsForm(ModelForm):
#     class Meta:
#         model = RemoteControlCommandAlertSettings
#         unique_together = ("user", "alert_type")
#         fields = (
#             "alert_methods",
#             "enabled",
#             "alert_methods",
#             "print_start",
#             "print_stop",
#             "print_pause",
#             "print_resume",
#             "monitoring_start",
#             "monitoring_stop",
#             "move_nozzle",
#         )


# class DiscordMethodSettingsForm(ModelForm):
#     class Meta:
#         model = DiscordMethodSettings
#         unique_together = ("user", "target_id", "target_id_type")
#         fields = ("target_id", "target_id_type")
