import logging
from asgiref.sync import async_to_sync
from django.dispatch import receiver
from django.db.models.signals import post_save
from channels.layers import get_channel_layer
from rest_framework.renderers import JSONRenderer

from print_nanny_webapp.devices.services import update_or_create_cloudiot_device


from .models import Device, PublicKey, TaskStatus, Task, OnboardingTask
from .enum import (
    TaskType,
    OnboardingTaskType,
    TaskStatusType,
)
from .api.serializers import TaskSerializer

logger = logging.getLogger(__name__)

# when PublicKey is created, automatically create/update CloudiotDevice with key


@receiver(post_save, sender=PublicKey, dispatch_uid="public_key_create_cloudiotdevice")
def create_public_key_cloudiotdevice(sender, instance: PublicKey, created, **kwargs):
    if created:
        update_or_create_cloudiot_device(instance)


# when device is created, automatically create OnboardingTask with type LINK
@receiver(post_save, sender=Device, dispatch_uid="create_device_link_task")
def create_device_link_task(sender, instance, created, **kwargs):
    if created:
        OnboardingTask.objects.create(
            task_type=OnboardingTaskType.LINK,
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
    async_to_sync(channel_layer.group_send)(
        instance.task.device.user.event_channel, payload
    )
