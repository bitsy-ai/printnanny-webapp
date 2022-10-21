from django.apps import AppConfig


class DevicesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "print_nanny_webapp.devices"

    def ready(self):
        try:
            import print_nanny_webapp.devices.signals  # noqa F401
        except ImportError:
            pass
        # import corsheaders check_request_enabled signal, which permits requests from any origin to interact with /api/ routes
        import print_nanny_webapp.utils.cors
