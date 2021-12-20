import logging
from asgiref.sync import async_to_sync
from django.dispatch import receiver
from django.db.models.signals import post_save
from channels.layers import get_channel_layer
from rest_framework.renderers import JSONRenderer

from .models import Device, TaskStatus, Task
from .enum import (
    TaskType,
    TaskStatusType,
)
from .api.serializers import TaskSerializer

logger = logging.getLogger(__name__)

# when device is created, automatically create Task with type ACTIVATE_LICENSE
@receiver(post_save, sender=Device, dispatch_uid="create_task_check_license")
def create_license_activate_task(sender, instance, created, **kwargs):
    if created:
        Task.objects.create(
            task_type=TaskType.CHECK_LICENSE,
            device=instance,
        )


# when Task is created, automatically create first status in WAITING state
@receiver(post_save, sender=Task, dispatch_uid="create_task_requested_status")
def create_task_requested_status(sender, instance, created, **kwargs):
    logger.info(
        f"create_task_requested_status sender={sender} instance={instance} created={created} kwargs={kwargs}"
    )
    # if task was created without a status, initialize status to PENDING (requires acknowledgement from device)
    if created:
        TaskStatus.objects.create(status=TaskStatusType.PENDING, task=instance)


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

    # send task to websocket channel
    channel_layer = get_channel_layer()
    serializer = TaskSerializer(instance=instance.task)
    data = JSONRenderer().render(serializer.data)
    layer = f"device_{instance.task.device.id}"

    payload = dict(type="task.status", data=serializer.data)
    logger.info(f"Sending to layer={layer} payload={payload}")
    async_to_sync(channel_layer.group_send)(layer, payload)
