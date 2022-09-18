import json
import pathlib
import os
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model

from djstripe.models import Customer

from print_nanny_webapp.shop.services import (
    build_stripe_checkout_session_customer_extra_kwargs,
)

User = get_user_model()


class TestShopServices(TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.factory = RequestFactory()

    def test_stripe_checkout_session_extra_kwargs_anon_new_customer(self):
        request = self.factory.post("/api/shop/orders")
        # request.user is not authenticated
        request.user = AnonymousUser()
        email = "new-customer@test.com"

        kwargs = build_stripe_checkout_session_customer_extra_kwargs(request, email)
        assert kwargs.get("customer_email") == email
        assert kwargs.get("customer_creation") == "always"

    def test_stripe_checkout_session_extra_kwargs_anon_existing_customer(self):
        """
        Tests checkout by an existing customer who is not authenticated/logged in
        """
        request = self.factory.post("/api/shop/orders")
        # request.user is not authenticated
        request.user = AnonymousUser()
        email = "john.doe@example.com"
        # test provided email already associated with an existing stripe customer
        user = User.objects.create(  # type: ignore[has-type]
            email=email, password="testing1234", is_superuser=False
        )
        # load fixture data
        with open(
            os.path.join(
                pathlib.Path().resolve(),
                "print_nanny_webapp/shop/tests/fixtures/customer_cus_4QWKsZuuTHcs7X.json",
            ),
            "r",
            encoding="utf-8",
        ) as f:

            fixture_data = json.load(f)

        customer = Customer.sync_from_stripe_data(fixture_data)
        customer.subscriber = user
        customer.save()

        # extra kwargs should include Stripe customer id, which will be passed to checkout session for continuity
        kwargs = build_stripe_checkout_session_customer_extra_kwargs(request, email)
        assert kwargs["customer"] == customer.id
        assert kwargs["client_reference_id"] == user.id

    def test_stripe_checkout_session_extra_kwargs_authenticated_existing_customer(self):
        """
        Tests checkout by an existing customer who is already authenticated
        """
        request = self.factory.post("/api/shop/orders")
        email = "john.doe@example.com"
        # test provided email already associated with an existing stripe customer
        user = User.objects.create(  # type: ignore[has-type]
            email=email, password="testing1234", is_superuser=False
        )
        request.user = user

        # load fixture data
        with open(
            os.path.join(
                pathlib.Path().resolve(),
                "print_nanny_webapp/shop/tests/fixtures/customer_cus_4QWKsZuuTHcs7X.json",
            ),
            "r",
            encoding="utf-8",
        ) as f:

            fixture_data = json.load(f)

        customer = Customer.sync_from_stripe_data(fixture_data)
        customer.subscriber = user
        customer.save()

        # extra kwargs should include Stripe customer id, which will be passed to checkout session for continuity
        kwargs = build_stripe_checkout_session_customer_extra_kwargs(request, email)
        assert kwargs["customer"] == customer.id
        assert kwargs["client_reference_id"] == user.id
