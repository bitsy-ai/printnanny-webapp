from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import manager
from polymorphic.models import PolymorphicModel

from .fields import MembershipTagType

User = get_user_model()


class UserTag(PolymorphicModel):
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class MembershipTag(UserTag):

    value = models.CharField(max_length=36, choices=MembershipTagType.choices)
