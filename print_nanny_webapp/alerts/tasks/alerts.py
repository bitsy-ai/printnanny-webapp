from typing import Union

from django.apps import apps
from print_nanny_webapp.alerts.api.serializer import AlertSerializer
from print_nanny_webapp.partners.api.serializer import (
    PartnerAlertSerializer,
    PartnersEnum,
)

AlertModel = apps.get_model("alerts", "Alert")


class AlertTask:
    """
    Serializes Alert instance to JSON payload
    Triggers various alert methods with payload data
    """

    serializer = AlertSerializer
    partner_serializer = PartnerAlertSerializer

    email_body_txt_template = "email/generic_alert_body.txt"
    email_body_html_template = (
        None  # @todo work with freelance designer on html email template set
    )
    email_subject_template = "email/generic_alert_subject.txt"

    def __init__(self, instance: AlertModel):
        self.instance = instance
        self.alert_trigger_method_map = {
            AlertModel.AlertMethodChoices.UI: self.trigger_ui_alert,
            AlertModel.AlertMethodChoices.EMAIL: self.trigger_email_alert,
            AlertModel.AlertMethodChoices.DISCORD: self.trigger_discord_alert,
            AlertModel.AlertMethodChoices.GEEKS3D: self.trigger_geeks3d_alert,
        }

    def trigger_alert(self) -> bool:
        """
        Returns a bool expressing whether method call resulted in alert being triggered
        Duplicate alert triggers will be ignored
        """
        if self.sent is False:
            self.alert_trigger_method_map[alert_method]()
            self.sent = True
            self.save()
            return True
        return False

    def get_serializer(self) -> Union[AlertSerializer, PartnerAlertSerializer]:
        if self.instance.alert_method.value in PartnersEnum:
            return self.partner_serializer(self.instance)
        return self.serializer(self.instance)

    def trigger_ui_alert(self):
        serializer = self.get_serializer()
        data = serializer.data

        channel_layer = get_channel_layer()

        # vuex namespace
        data["namespace"] = "alerts_dropdown"
        # required by websocket message handler in vue app(s)
        data["action"] = "alertMessage"

        async_to_sync(channel_layer.group_send)(
            f"alerts_{self.user.id}",
            {
                "type": "alert.message",
                # https://github.com/nathantsoi/vue-native-websocket#with-format-json-enabled
                "data": JSONRenderer().render(data),
            },
        )

    def trigger_email_alert(self) -> AnymailMessage:
        serializer = self.get_serializer()
        data = serializer.data

        device_url = reverse(
            "dashboard:octoprint-devices:detail",
            kwargs={"pk": self.octoprint_device.id},
        )
        merge_data = {
            "DEVICE_URL": device_url,
            "FIRST_NAME": self.user.first_name or "Maker",
            "DEVICE_NAME": self.octoprint_device.name,
            "ALERT_TYPE": self.get_alert_type_display(),
        }

        text_body = render_to_string(self.email_body_txt_template, merge_data)
        subject = render_to_string(self.email_subject_template, merge_data)

        message = AnymailMessage(
            subject=subject,
            body=text_body,
            to=[self.user.email],
            tags=[
                self.__class__,
                f"User:{self.user.id}",
                f"Device:{self.octoprint_device.id}",
            ],
        )

        return message

    def trigger_alerts_task(self):
        serializer = self.get_serializer()

        self.print_session.status = self.print_session.StatusChoices.DONE
        self.print_session.save()
        return trigger_alerts_task.delay(self.id, serializer.data)

    def trigger_discord_alert(self):
        serializer = self.get_serializer()
        data = serializer.data

        channel_layer = get_channel_layer()
        discord_settings = DiscordMethodSettings.objects.filter(user=self.instance.user)

        channel_ids = []
        user_ids = []

        for setting in discord_settings:
            if setting.target_id_type == DiscordMethodSettings.TargetIDTypeChoices.USER:
                user_ids.append(setting.target_id)
            elif (
                setting.target_id_type
                == DiscordMethodSettings.TargetIDTypeChoices.CHANNEL
            ):
                channel_ids.append(setting.target_id)

        logger.info(
            f"Sending Discord alert to channels: {channel_ids} and users: {user_ids}"
        )

        message = f"{data['title']}: {data['description']}"
        if data.get("manage_device_url") is not None:
            message += "\n" + data["manage_device_url"]

        async_to_sync(channel_layer.send)(
            "discord",
            {
                "type": "trigger.alert",
                "user_ids": user_ids,
                "channel_ids": channel_ids,
                "message": message,
            },
        )


class RemoteCommandStatusAlertTask(AlertTask):
    """
    Fires when the status of a remote command changes
    Status choices governed by RemoteControlCommandAlertSettings.AlertSubTypeChoices { RECEVIED, FAILED, SUCCESS }
    """

    email_body_txt_template = "email/remote_control_command_body.txt"
    email_body_html_template = (
        None  # @todo work with freelance designer on html email template set
    )
    email_subject_template = "email/remote_control_command_subject.txt"

    def trigger_email_alert(self):

        merge_data = {
            "FIRST_NAME": self.instance.user.first_name or "Maker",
            "DEVICE_NAME": self.instance.command.device.name,
            "COMMAND": self.instance.command.command,
            "SUBTYPE": self.instance.alert_subtype,
            "PROGRESS": self.instance.command.metadata.get("progress"),
            "MANAGE_DEVICE_URL": self.instance.command.device.manage_url,
        }

        text_body = render_to_string(self.email_body_txt_template, merge_data)
        subject = render_to_string(self.email_subject_template, merge_data)

        message = AnymailMessage(
            subject=subject,
            body=text_body,
            to=[self.instance.user.email],
            tags=[
                "RemoteControlCommandAlert",
                self.instance.command.command,
                self.instance.alert_subtype,
                f"User:{self.instance.user.id}",
            ],
        )
        message.send()

        return message


class PrintSessionAlertTask(AlertTask):

    email_body_txt_template = "email/remote_control_command_body.txt"
    email_body_html_template = (
        None  # @todo work with freelance designer on html email template set
    )
    email_subject_template = "email/remote_control_command_subject.txt"

    def trigger_email_alert(self):

        device_url = reverse(
            "dashboard:octoprint-devices:detail",
            kwargs={"pk": self.instance.octoprint_device.id},
        )
        merge_data = {
            "DEVICE_URL": device_url,
            "FIRST_NAME": self.instance.user.first_name or "Maker",
            "DEVICE_NAME": self.instance.octoprint_device.name,
            # TODO session url view
            "ANNOTATED_VIDEO_URL": self.instance.dashboard_url,
        }
        text_body = render_to_string(self.instance.email_body_txt_template, merge_data)
        subject = render_to_string(self.instance.email_subject_template, merge_data)
        message = AnymailMessage(
            subject=subject,
            body=text_body,
            to=[self.instance.user.email],
            tags=[
                self.__class__,
                f"User:{self.instance.user.id}",
                f"Device:{self.instance.octoprint_device.id}",
                f"PrintSessionID:{self.instance.print_session.id}",
                f"PrintSession:{self.instance.print_session.session}",
            ],
        )
        message.send()
        return message
