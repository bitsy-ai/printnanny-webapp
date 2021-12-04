from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Device, TaskStatus, Task
from .choices import (
    TaskType,
    TaskStatusType,
)

# when device is created, automatically create Task with type ACTIVATE_LICENSE
@receiver(post_save, sender=Device, dispatch_uid="create_system_task_activate_license")
def create_license_activate_system_task(sender, instance, created, **kwargs):
    if created:
        Task.objects.create(
            task_type=TaskType.ACTIVATE_LICENSE,
            device=instance,
        )


# when Task is created, automatically create first status in WAITING state
@receiver(post_save, sender=Task, dispatch_uid="create_system_task_status_waiting")
def create_license_activate_system_task_status(sender, instance, created, **kwargs):
    if created:
        TaskStatus.objects.create(status=TaskStatusType.REQUESTED, system_task=instance)
