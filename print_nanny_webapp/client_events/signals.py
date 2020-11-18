from anymail.signals import tracking
from django.dispatch import receiver


# Mailgun will report these Anymail event_types: delivered, rejected, bounced, complained, unsubscribed, opened, clicked.



@receiver(tracking)
def handle_open(self, event, esp_name, **kwargs):
    if event.event_type == 'open':
        pass


@receiver(tracking)
def handle_click(self, event, esp_name, **kwargs):
    if event.event_type == 'click':
        pass