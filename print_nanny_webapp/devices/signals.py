from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Device, SystemTaskStatus, SystemTask
from .choices import (
    SystemTaskType,
    SystemTaskStatusType,
)

# when device is created, automatically create SystemTask with type ACTIVATE_LICENSE
@receiver(post_save, sender=Device, dispatch_uid="create_system_task_activate_license")
def create_license_activate_system_task(sender, instance, created, **kwargs):
    if created:
        SystemTask.objects.create(
            task_type=SystemTaskType.ACTIVATE_LICENSE,
            device=instance,
        )


# when SystemTask is created, automatically create first status in WAITING state
@receiver(
    post_save, sender=SystemTask, dispatch_uid="create_system_task_status_waiting"
)
def create_license_activate_system_task_status(sender, instance, created, **kwargs):
    if created:
        SystemTaskStatus.objects.create(
            status=SystemTaskStatusType.REQUESTED, system_task=instance
        )
