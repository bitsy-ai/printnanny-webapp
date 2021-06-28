import pytest
from pytest_django.asserts import assertRedirects
from django.test import RequestFactory
from print_nanny_webapp.users.models import User
from print_nanny_webapp.utils.views import SubscriptionRequiredMixin
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import PermissionDenied
from django.urls import reverse


@pytest.mark.django_db
def test_checkout_redirects_anonymous_user(client):
    url = reverse("subscriptions:checkout")
    response = client.get(url)
    assertRedirects(
        response,
        "/subscriptions/signup?next=/subscriptions/checkout",
    )


@pytest.mark.django_db
def test_sold_out_redirect(user: User, client, settings: "django.conf.settings"):
    settings.PAID_BETA_SUBSCRIPTION_LIMIT = 0
    client.force_login(user)
    response = client.get("/subscriptions/signup")
    assertRedirects(response, "/subscriptions/sold-out")
    response = client.get("/subscriptions/checkout")
    assertRedirects(response, "/subscriptions/sold-out")


@pytest.mark.django_db
def test_membership_available(user: User, client, settings: "django.conf.settings"):
    settings.PAID_BETA_SUBSCRIPTION_LIMIT = 10
    client.force_login(user)
    response = client.get("/subscriptions/checkout")
    assert response.status_code == 200


@pytest.mark.django_db
def test_subscription_required_mixin(user: User, rf: RequestFactory):
    class AView(SubscriptionRequiredMixin, View):
        def get(self, request, *args, **kwargs):
            return HttpResponse()

    request = rf.get("/foo")
    request.user = AnonymousUser()

    # users not logged in redirected to login screen
    view = AView.as_view()
    response = view(request)
    assert response.status_code == 302
    assert "/accounts/login/?next=/foo" == response.url

    request = rf.get("/foo")
    request.user = user
    with pytest.raises(PermissionDenied):
        view(request)
