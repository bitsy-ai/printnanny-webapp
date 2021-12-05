import logging
from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Device, TaskStatus, Task
from .choices import (
    TaskType,
    TaskStatusType,
)

logger = logging.getLogger(__name__)

# when device is created, automatically create Task with type ACTIVATE_LICENSE
@receiver(post_save, sender=Device, dispatch_uid="create_task_activate_license")
def create_license_activate_task(sender, instance, created, **kwargs):
    if created:
        Task.objects.create(
            task_type=TaskType.ACTIVATE_LICENSE,
            device=instance,
        )


# when Task is created, automatically create first status in WAITING state
@receiver(post_save, sender=Task, dispatch_uid="create_task_requested_status")
def create_task_requested_status(sender, instance, created, **kwargs):
    logger.info(
        f"create_task_requested_status sender={sender} instance={instance} created={created} kwargs={kwargs}"
    )
    if created:
        TaskStatus.objects.create(status=TaskStatusType.REQUESTED, task=instance)


# when TaskStatus is created, update Task.active parent field
@receiver(post_save, sender=TaskStatus, dispatch_uid="update_task_active_field")
def update_task_active_field(sender, instance, created, **kwargs):
    logger.info(
        f"update_task_active_field sender={sender} instance={instance} created={created} kwargs={kwargs}"
    )

    if instance.status in (
        TaskStatusType.FAILED,
        TaskStatusType.SUCCESS,
        TaskStatusType.TIMEOUT,
    ):
        instance.task.active = False
        instance.task.save()
