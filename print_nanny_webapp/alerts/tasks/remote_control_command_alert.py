
from django.apps import apps
from celery import group, shared_task, chain
from django.contrib.auth import get_user_model

User = get_user_model()
RemoteControlCommand = apps.get_model('remote_control', 'RemoteControlCommand')
RemoteControlCommandAlert = apps.get_model('alerts', 'RemoteControlCommandAlert')
RemoteControlCommandAlertSettings = apps.get_model('alerts', 'RemoteControlCommandAlertSettings')

@shared_task
def create_remote_control_command_alerts(user_id, command_id, alert_subtype):


    user = Users.get(id=user_id)
    command = RemoteControlCommand(id=command_id)

    alert_settings = RemoteControlCommandAlertSettings(user=user)
    alert_settings_attr = alert_settings.command_to_attr(command.command)

    created_alerts = []
    if alert_subtype in alert_settings_attr:
        instance = super().create(*args, **kwargs)
        instance.send_alerts(alert_settings.alert_methods)
        
        return instance
    alerts = RemoteControlCommandAlert.objects.create(
        user_id=user_id,
        command_id=command_id,
        alert_subtype=alert_subtype,
    )
    return created_alerts



