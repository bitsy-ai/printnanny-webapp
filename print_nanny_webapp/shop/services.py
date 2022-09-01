from uuid import uuid4
from django.conf import settings
from django.http.request import HttpRequest

from djstripe.models.core import (
    Customer as DjStripeCustomer,
)
from djstripe.settings import djstripe_settings
from djstripe.models.checkout import Session as DjStripeCheckoutSession

import stripe

from print_nanny_webapp.shop.models import Product, Order


def sync_stripe_checkout_session(session_id: str) -> DjStripeCheckoutSession:
    stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY

    stripe_res = stripe.checkout.Session.retrieve(session_id)
    # sync djstripe model from response, then return djstripe model to be serialized
    return Session.sync_from_stripe_data(stripe_res)


def sync_stripe_customer_by_id(stripe_customer_id: str) -> DjStripeCustomer:
    stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY

    stripe_res = stripe.DjStripeCustomer.retrieve(stripe_customer_id)
    return DjStripeCustomer.sync_from_stripe_data(stripe_res)


def create_stripe_checkout_session(request: HttpRequest, product: Product, email: str):
    """
    Attempt to create a Stripe checkout session for product_name

    """
    stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY
    django_session_key = request.session._get_or_create_session_key()

    # prices = stripe.Price.list(lookup_keys=[stripe_lookup_key])

    # try to get Stripe customer from user
    user = None
    customer = None
    order_id = uuid4()

    # add django session key to stripe metadata
    extra_kwargs = dict(
        # expand customer and payment_intent fields in response
        expand=["customer", "payment_intent"],
        metadata=dict(
            django_session_key=django_session_key,
            django_product_id=product.id,
            django_order_id=order_id,
        ),
    )
    if request.user.is_authenticated:
        user = request.user
        # provides djstripe_subscriber_user reverse relationship
        extra_kwargs["metadata"][djstripe_settings.SUBSCRIBER_CUSTOMER_KEY] = user.id
        # an extra reference id
        extra_kwargs["client_reference_id"] = user.id
        try:
            customer = DjStripeCustomer.objects.get(subscriber=user)
            extra_kwargs["customer"] = customer.id

        # customer not found
        except DjStripeCustomer.DoesNotExist:
            extra_kwargs["customer_email"] = email
    else:
        try:
            customer = DjStripeCustomer.objects.get(email=email)
            extra_kwargs["customer"] = customer.id
        # customer not found
        except DjStripeCustomer.DoesNotExist:
            extra_kwargs["customer_email"] = email

    if product.slug == "sdwire":
        price_id = product.prices.all()[0].id

        # set success / cancel urls
        extra_kwargs["success_url"] = request.build_absolute_uri(
            "/shop/sdwire/success/"
        )
        # add "{CHECKOUT_SESSION_ID}" template string to url. this gets uri-encoded to %7B if passed to build_absolute_uri fn
        extra_kwargs["success_url"] += "{CHECKOUT_SESSION_ID}"

        extra_kwargs["cancel_url"] = request.build_absolute_uri("/shop/sdwire")

        # quick hack to replace :8000 server-side port with front-end hot module reload port (in dev mode)
        if settings.DEBUG:
            extra_kwargs["success_url"] = extra_kwargs["success_url"].replace(
                ":8000", ":3000"
            )
            extra_kwargs["cancel_url"] = extra_kwargs["success_url"].replace(
                ":8000", ":3000"
            )

        return (
            stripe.checkout.Session.create(
                customer_creation="always",
                payment_method_types=["card"],
                payment_intent_data={
                    # off_session indicates
                    "setup_future_usage": "off_session",
                    "metadata": extra_kwargs["metadata"],
                },
                line_items=[
                    {
                        "price": price_id,
                        "adjustable_quantity": {
                            "enabled": True,
                            "minimum": 1,
                            "maximum": 10,
                        },
                        "quantity": 1,
                    }
                ],
                mode="payment",
                billing_address_collection="required",
                shipping_address_collection=dict(
                    allowed_countries=[
                        "US",
                        "CA",
                    ]
                ),
                shipping_options=[
                    {
                        "shipping_rate_data": {
                            "type": "fixed_amount",
                            "fixed_amount": {
                                "amount": 999,
                                "currency": "usd",
                            },
                            "display_name": "USPS Ground",
                        }
                    },
                ],
                **extra_kwargs,
            ),
            order_id,
        )
    else:
        raise NotImplementedError(
            f"create_stripe_checkout_session not implemented for Products={product}"
        )


def create_order(request: HttpRequest, product: Product, email: str):
    checkout_session_res, order_id = create_stripe_checkout_session(
        request, product, email
    )
    checkout_session_redirect = checkout_session_res.url
    checkout_session = DjStripeCheckoutSession.sync_from_stripe_data(
        checkout_session_res
    )
    order = Order.objects.create(
        djstripe_customer=checkout_session.customer,
        djstripe_checkout_session=checkout_session,
        djstripe_payment_intent=checkout_session.payment_intent,
        id=order_id,
    )
    order.products.add(product)
    order.stripe_checkout_redirect_url = checkout_session_redirect
    return order
