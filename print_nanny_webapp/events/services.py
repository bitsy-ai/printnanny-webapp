import logging

from django.apps import apps
from anymail.message import AnymailMessage

from uuid import UUID


PrintJobAlert = apps.get_model("events", "PrintJobAlert")

logger = logging.getLogger(__name__)


def send_print_job_alert_email(print_job_alert_id: UUID):
    alert = PrintJobAlert.objects.get(id=print_job_alert_id)

    msg = AnymailMessage(
        subject=alert.email_subject(),
        tags=(
            "model:PrintJobAlert",
            f"event_source:{alert.event_source}",
            f"event_type:{alert.event_type}",
        ),
        from_email="PrintNanny <no-reply@mail.printnanny.ai>",
        template_id=PrintJobAlert.EMAIL_TEMPLATE_ID,
        to=[alert.user.email],
        merge_metadata={alert.user.email: alert.email_merge_data()},
    )
    msg.send(fail_silently=False)
    recipient = msg.anymail_status.recipients[alert.user.email]
    logger.info(
        "Success! Sent alert id=%s event_type=%s recipient=%s",
        alert.id,
        alert.event_type,
        recipient,
    )
    alert.email_message_id = recipient.message_id
