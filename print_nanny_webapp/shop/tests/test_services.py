from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser

from django.contrib.auth import get_user_model
from print_nanny_webapp.shop.services import (
    build_stripe_checkout_session_customer_extra_kwargs,
)

User = get_user_model()


class TestShopServices(TestCase):
    def setUp(self) -> None:
        super().setUp()
        # self.user = User.objects.create(
        #     email="new-customer@test.com", password="testing1234", is_superuser=False
        # )
        self.factory = RequestFactory()

    def test_stripe_checkout_session_extra_kwargs_anon_new_customer(self):
        request = self.factory.post("/api/shop/orders")
        # request.user is not authenticated
        request.user = AnonymousUser()
        email = "new-customer@test.com"

        kwargs = build_stripe_checkout_session_customer_extra_kwargs(request, email)
        assert kwargs.get("customer_email") == email
        assert kwargs.get("customer_creation") == "always"
