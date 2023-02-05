import json
import pathlib
import os
from uuid import uuid4

from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model

from djstripe.models import Customer

from print_nanny_webapp.shop.services import (
    build_stripe_checkout_session_kwargs_v1,
)
from print_nanny_webapp.shop.models import Product

User = get_user_model()


class TestSubscriptionBadges(TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.factory = RequestFactory()

    def test_badges_anon_new_customer(self):
        request = self.factory.get("/api/shop/orders")
        request.user = AnonymousUser()
        request.session = self.client.session
        email = "new-customer@test.com"


class TestShopServices(TestCase):
    fixtures = [
        "/app/print_nanny_webapp/shop/tests/fixtures/djstripe_account.json",
        "/app/print_nanny_webapp/shop/tests/fixtures/djstripe_product.json",
        "/app/print_nanny_webapp/shop/tests/fixtures/djstripe_price.json",
        "/app/print_nanny_webapp/shop/tests/fixtures/shop_product.json",
    ]

    def setUp(self) -> None:
        super().setUp()

        self.factory = RequestFactory()

    def test_shippable_product_anon_new_customer(self):
        request = self.factory.post("/api/shop/orders")
        # request.user is not authenticated
        request.user = AnonymousUser()
        request.session = self.client.session
        email = "new-customer@test.com"
        order_id = str(uuid4())

        product = Product.objects.filter(is_shippable=True).first()

        kwargs = build_stripe_checkout_session_kwargs_v1(
            request, email, order_id, product
        )
        assert kwargs.get("customer_email") == email
        assert kwargs.get("customer_creation") == "always"
        assert kwargs.get("mode") == "payment"

    def test_subscription_product_anon_new_customer(self):
        request = self.factory.post("/api/shop/orders")
        # request.user is not authenticated
        request.user = AnonymousUser()
        request.session = self.client.session
        email = "new-customer@test.com"
        order_id = str(uuid4())

        product = Product.objects.filter(is_subscription=True).first()

        kwargs = build_stripe_checkout_session_kwargs_v1(
            request, email, order_id, product
        )
        assert kwargs.get("customer_email") == email
        assert kwargs.get("customer_creation") is None
        assert kwargs.get("mode") == "subscription"

    def test_shippable_product_anon_existing_customer(self):
        """
        Tests checkout by an existing customer who is not authenticated/logged in
        """
        request = self.factory.post("/api/shop/orders")
        # request.user is not authenticated
        request.user = AnonymousUser()
        request.session = self.client.session

        email = "john.doe@example.com"
        # test provided email already associated with an existing stripe customer
        user = User.objects.create(  # type: ignore[has-type]
            email=email, password="testing1234", is_superuser=False
        )
        order_id = str(uuid4())

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
        product = Product.objects.filter(is_shippable=True).first()

        # extra kwargs should include Stripe customer id, which will be passed to checkout session for continuity
        kwargs = build_stripe_checkout_session_kwargs_v1(
            request, email, order_id, product
        )
        assert kwargs["customer"] == customer.id
        assert kwargs["client_reference_id"] == user.id
        assert kwargs.get("mode") == "payment"
        assert kwargs.get("shipping_options") is not None

    def test_subscription_product_anon_existing_customer(self):
        """
        Tests checkout by an existing customer who is not authenticated/logged in
        """
        request = self.factory.post("/api/shop/orders")
        # request.user is not authenticated
        request.user = AnonymousUser()
        request.session = self.client.session

        email = "john.doe@example.com"
        # test provided email already associated with an existing stripe customer
        user = User.objects.create(  # type: ignore[has-type]
            email=email, password="testing1234", is_superuser=False
        )
        order_id = str(uuid4())

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
        product = Product.objects.filter(is_subscription=True).first()

        # extra kwargs should include Stripe customer id, which will be passed to checkout session for continuity
        kwargs = build_stripe_checkout_session_kwargs_v1(
            request, email, order_id, product
        )
        assert kwargs["customer"] == customer.id
        assert kwargs["client_reference_id"] == user.id
        assert kwargs.get("mode") == "subscription"

    def test_shippable_product_authenticated_existing_customer(self):
        """
        Tests checkout by an existing customer who is already authenticated
        """
        request = self.factory.post("/api/shop/orders")
        email = "john.doe@example.com"
        password = "testing1234"
        # test provided email already associated with an existing stripe customer
        user = User.objects.create(  # type: ignore[has-type]
            email=email, password=password, is_superuser=False
        )
        request.user = user
        # login user so self.client.session reflects
        # self.client.login sets up self.client.session to be usable
        self.client.login(email=email, password=password)
        request.session = self.client.session

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
        order_id = str(uuid4())
        product = Product.objects.filter(is_shippable=True).first()

        # extra kwargs should include Stripe customer id, which will be passed to checkout session for continuity
        kwargs = build_stripe_checkout_session_kwargs_v1(
            request, email, order_id, product
        )
        assert kwargs["customer"] == customer.id
        assert kwargs["client_reference_id"] == user.id
        assert kwargs.get("mode") == "payment"
        assert kwargs.get("shipping_options") is not None

    def test_subscription_product_authenticated_existing_customer(self):
        """
        Tests checkout by an existing customer who is already authenticated
        """
        request = self.factory.post("/api/shop/orders")
        email = "john.doe@example.com"
        password = "testing1234"
        # test provided email already associated with an existing stripe customer
        user = User.objects.create(  # type: ignore[has-type]
            email=email, password=password, is_superuser=False
        )
        request.user = user
        # login user so self.client.session reflects
        # self.client.login sets up self.client.session to be usable
        self.client.login(email=email, password=password)
        request.session = self.client.session

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
        order_id = str(uuid4())
        product = Product.objects.filter(is_subscription=True).first()

        # extra kwargs should include Stripe customer id, which will be passed to checkout session for continuity
        kwargs = build_stripe_checkout_session_kwargs_v1(
            request, email, order_id, product
        )
        assert kwargs["customer"] == customer.id
        assert kwargs["client_reference_id"] == user.id
        assert kwargs.get("mode") == "subscription"
