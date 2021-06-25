import pytest
from pytest_django.asserts import assertRedirects
from django.test import RequestFactory, TestCase
from print_nanny_webapp.users.tests.factories import UserFactory
from print_nanny_webapp.users.models import User
from print_nanny_webapp.subscriptions.views import (
    SubscriptionSoldoutView,
    SubscriptionFoundingMemberView,
)


@pytest.mark.django_db
def test_sold_out_redirect(user: User, client, settings: "django.conf.settings"):
    settings.PAID_BETA_SUBSCRIPTION_LIMIT = 0
    client.force_login(user)
    response = client.get("/subscriptions/founding-member")
    assertRedirects(response, "/subscriptions/sold-out")


@pytest.mark.django_db
def test_no_sold_out_redirect(user: User, client, settings: "django.conf.settings"):
    settings.PAID_BETA_SUBSCRIPTION_LIMIT = 10
    client.force_login(user)
    response = client.get("/subscriptions/founding-member")
    assert response.status_code == 200
