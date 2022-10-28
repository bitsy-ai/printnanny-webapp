from anymail.signals import post_send
from django.dispatch import receiver

from print_nanny_webapp.email_campaigns.models import EmailMessage


@receiver(post_send)
def log_sent_message(sender, message, status, esp_name, **kwargs):
    # This assumes you've implemented a SentMessage model for tracking sends.
    # status.recipients is a dict of email: status for each recipient
    for email, recipient_status in status.recipients.items():
        EmailMessage.objects.create(
            esp=esp_name,
            message_id=recipient_status.message_id,  # might be None if send failed
            email=email,
            subject=message.subject,
            status=recipient_status.status,
        )
