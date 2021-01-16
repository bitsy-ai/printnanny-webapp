from django.apps import AppConfig
from health_check.plugins import plugin_dir


class RemoteControlConfig(AppConfig):
    name = "print_nanny_webapp.remote_control"

    def ready(self):
        try:
            import print_nanny_webapp.remote_control.signals  # noqa F401
        except ImportError:
            pass

        # from print_nanny_webapp.utils.healthcheck import RemoteControlEventCheck
        # plugin_dir.register(RemoteControlEventCheck)
