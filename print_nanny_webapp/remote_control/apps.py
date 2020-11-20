from django.apps import AppConfig


class RemoteControlConfig(AppConfig):
    name = 'print_nanny_webapp.remote_control'
    # def ready(self):
    #     try:
    #         import print_nanny_webapp.remote_control.signals  # noqa F401
    #     except ImportError:
    #         pass
