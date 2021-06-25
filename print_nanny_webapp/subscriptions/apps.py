from django.apps import AppConfig


class SubscriptionsConfig(AppConfig):
    name = "print_nanny_webapp.subscriptions"
    verbose_name = "Stripe subscriptions"

    def ready(self):
        try:
            import print_nanny_webapp.subscriptions.tasks  # noqa F401
        except ImportError:
            pass
