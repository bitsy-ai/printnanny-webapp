from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from print_nanny_webapp.workspaces.services import create_personal_workspace

User = get_user_model()


@receiver(post_save, sender=User)
def create_personal_workspace_for_new_user(sender, instance, created, **kwargs):
    if created:
        create_personal_workspace(instance)
