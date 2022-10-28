from django.apps import AppConfig


class EmailCampaignsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "print_nanny_webapp.email_campaigns"

    def ready(self):
        import print_nanny_webapp.email_campaigns.signals
