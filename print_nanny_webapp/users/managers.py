import logging
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.db import models

logger = logging.getLogger(__name__)

class InviteRquestManager(models.Manager):
    def create(self, **kwargs):
        from .tasks import create_ghost_members

        instance = super().create(**kwargs)
        task = create_ghost_members.delay([instance.to_ghost_member()])
        logger.info(f'Submitted create_ghost_members with task.id={task.id}')

        return instance

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        from .tasks import create_ghost_members

        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        task = create_ghost_members.delay([user.to_ghost_member()])
        logger.info(f'Submitted create_ghost_members with task.id={task.id}')
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        from .tasks import create_ghost_members

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)
