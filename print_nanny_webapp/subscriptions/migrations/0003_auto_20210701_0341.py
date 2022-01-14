# Generated by Django 3.2.2 on 2021-07-01 03:41

from print_nanny_webapp.subscriptions.models import MemberBadge
from django.db import migrations
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import Q


def create_free_beta_member_badges(apps, schema_editor):
    MemberBadge = apps.get_model("subscriptions", "MemberBadge")
    User = get_user_model()

    max_id = list(settings.FREE_BETA_TESTER_IDS)[-1]

    users = User.objects.filter(Q(id__lte=max_id)).all()
    for user in users:
        MemberBadge.objects.create(user_id=user.id, type="FreeBeta")


class Migration(migrations.Migration):

    dependencies = [
        ("subscriptions", "0002_auto_20210625_0439"),
        ("users", "0002_user_is_serviceuser"),
    ]

    operations = [
        migrations.RunPython(create_free_beta_member_badges),
    ]
