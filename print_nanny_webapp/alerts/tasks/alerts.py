from typing import Optional, Union
from urllib.parse import urljoin
from django.apps import apps
from django.urls import reverse
from django.template import engines
import logging

import requests
from print_nanny_webapp.alerts.api.serializers import AlertSerializer
from print_nanny_webapp.partners.api.serializers import (
    Partner3DGeeksAlertSerializer,
    PartnersEnum,
)
from asgiref.sync import async_to_sync
from rest_framework.renderers import JSONRenderer

from django.conf import settings
from django.template.loader import render_to_string
from anymail.message import AnymailMessage
from django.template import Context, Template
from channels.layers import get_channel_layer

AlertMessage = apps.get_model("alerts", "AlertMessage")
AlertSettings = apps.get_model("alerts", "AlertSettings")
GeeksToken = apps.get_model("partners", "GeeksToken")

logger = logging.getLogger(__name__)


class AlertTask:
    """
    Serializes Alert instance to JSON payload
    Triggers various alert methods with payload data
    """

    def __init__(
        self,
        instance: AlertMessage,
        email_body_txt_template: str = "email/generic_alert_body.txt",
        email_body_html_template: Optional[str] = None,
        email_subject_template: str = "email/generic_alert_subject.txt",
        serializer=AlertSerializer,
        partner_3dgeeks_serializer=Partner3DGeeksAlertSerializer,
    ):
        self.instance = instance
        self.email_body_txt_template = email_body_txt_template
        self.email_body_html_template = email_body_html_template
        self.email_subject_template = email_subject_template
        self.serializer = serializer
        self.partner_3dgeeks_serializer = partner_3dgeeks_serializer
        self.alert_trigger_method_map = {
            AlertSettings.AlertMethod.UI: self.trigger_ui_alert,
            AlertSettings.AlertMethod.EMAIL: self.trigger_email_alert,
            AlertSettings.AlertMethod.DISCORD: self.trigger_discord_alert,
            AlertSettings.AlertMethod.PARTNER_3DGEEKS: self.trigger_geeks3d_alert,
        }

    def trigger_alert(self) -> bool:
        """
        Returns a bool expressing whether method call resulted in alert being triggered
        Duplicate alert triggers will be ignored
        """
        if self.instance.sent is False:
            self.alert_trigger_method_map[self.instance.alert_method]()
            self.instance.sent = True
            self.instance.save()
            return True
        return False

    def get_serializer(self) -> Union[AlertSerializer, Partner3DGeeksAlertSerializer]:
        if self.instance.alert_method is AlertSettings.AlertMethod.PARTNER_3DGEEKS:
            return self.partner_3dgeeks_serializer(self.instance)
        return self.serializer(self.instance)

    def trigger_geeks3d_alert(self):
        serializer = self.get_serializer()
        data = serializer.data
        token = data["token"]
        headers = {"Authorization": f"Bearer {token}"}
        logger.info(f"3DGeeks alerts_push headers={headers} request={data}")
        res = requests.post(
            settings.PARTNERS_3DGEEKS_SETTINGS["alerts_push"],
            json=data,
            headers=headers,
        )
        logger.warning(f"3DGeeks alerts_push response: {res.json()}")
        return res

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

    def trigger_email_alert(self):
        if self.instance.event_type is AlertMessage.AlertMessageType.TEST:
            merge_data = {
                "FIRST_NAME": self.instance.user.first_name or "Maker",
                "GCODE_FILENAME": "my_test_print.gcode",
                "DEVICE_NAME": "My Test Printer",
                "EVENT_TYPE": AlertMessage.AlertMessageType.TEST,
                "DEVICE_URL": urljoin(
                    settings.BASE_URL, "dashboard/octoprint-devices/"
                ),
                "PRINT_PROGRESS": "11%",
                "TIME_REMAINING": "23:23:59",
            }
            tags = [
                f"User:{self.instance.user.id}",
            ]
        else:
            device_url = reverse(
                "dashboard:octoprint-devices:detail",
                kwargs={"pk": self.instance.octoprint_device.id},
            )
            device_url = urljoin(settings.BASE_URL, device_url)
            serializer = self.get_serializer()
            data = serializer.data

            merge_data = {
                "DEVICE_URL": device_url,
                "FIRST_NAME": self.instance.user.first_name or "Maker",
                "DEVICE_NAME": self.instance.octoprint_device.name,
                "EVENT_TYPE": self.instance.event_type,
                "GCODE_FILENAME": self.instance.print_session.gcode_file,
            }
            if self.instance.event_type is AlertMessage.AlertMessageType.VIDEO_DONE:
                videos_url = reverse("dashboard:videos:list")
                videos_url = urljoin(settings.BASE_URL, videos_url)
                merge_data.update(
                    {
                        "VIDEO_DASHBOARD_URL": videos_url,
                        "TIME_ELAPSED": data["time_elapsed"],
                    }
                )
            else:
                merge_data.update(
                    {
                        "PRINT_PROGRESS": data["print_progress"],
                        "TIME_REMAINING": data["time_remaining"],
                    }
                )
            tags = [
                f"User:{self.instance.user.id}",
                f"Device:{self.instance.octoprint_device.id}",
                f"PrintSessionID:{self.instance.print_session.id}",
                f"PrintSession:{self.instance.print_session.session}",
            ]
        subject_end_template = Template(self.instance.get_event_type_display())
        ctx = Context(merge_data)

        merge_data.update({"EMAIL_SUBJECT": subject_end_template.render(ctx)})

        text_body = render_to_string(self.email_body_txt_template, merge_data)
        subject = render_to_string(self.email_subject_template, merge_data)
        message = AnymailMessage(
            subject=subject,
            body=text_body,
            to=[self.instance.user.email],
            tags=tags,
        )
        message.send()
        return message

    def trigger_discord_alert(self):
        raise NotImplementedError
