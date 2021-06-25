from django.test import TestCase
from django.contrib.auth import get_user_model
from print_nanny_webapp.analytics.signals import update_ghost_member_tag
from print_nanny_webapp.analytics.models import MembershipTag, MembershipTagType


class TestUserTagSignals(TestCase):
    def test_update_ghost_member_tag_receiver(self, mocker, user):
        mock_task = mocker.patch(
            "print_nanny_webapp.analytics.tasks.update_ghost_member_tag_task"
        )
        tag = MembershipTag.objects.create(user=user, value=MembershipTagType.BETA_PAID)

        assert mock_task.called
