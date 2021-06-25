import logging
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserTag, MembershipTag
from .tasks import update_ghost_member_tag_task

logger = logging.getLogger(__name__)


@receiver(post_save, sender=MembershipTag, dispatch_uid="update_ghost_member_tag")
def update_ghost_member_tag(sender, instance, **kwargs):
    return update_ghost_member_tag_task.delay(
        email=instance.user.email, tag=instance.value
    )
