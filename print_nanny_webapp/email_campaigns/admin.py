from django.contrib import admin

from print_nanny_webapp.email_campaigns.models import (
    Campaign,
    EmailTrackingEvent,
    EmailMessage,
)

# Register your models here.
@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ("created_dt", "template", "subject", "send_fn")
    model = Campaign


@admin.register(EmailTrackingEvent)
class EmailTrackingEventAdmin(admin.ModelAdmin):
    list_display = ("created_dt", "recipient", "email_message", "user", "campaign")
    model = EmailTrackingEvent


@admin.register(EmailMessage)
class EmailMessageAdmin(admin.ModelAdmin):
    list_display = ("message_id", "user", "email", "campaign", "send_status")
    model = EmailMessage
