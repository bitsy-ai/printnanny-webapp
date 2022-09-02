from uuid import uuid4
from typing import Dict, Any
from django.conf import settings
from django.http.request import HttpRequest

from djstripe.models.core import (
    Customer as DjStripeCustomer,
    PaymentIntent as DjStripePaymentIntent,
    Charge as DjStripeCharge,
)
from djstripe.settings import djstripe_settings
from djstripe.models.checkout import Session as DjStripeCheckoutSession


import stripe

from print_nanny_webapp.shop.models import OrderStatus, Product, Order
from print_nanny_webapp.shop.enum import OrderStatusType


def sync_stripe_checkout_session(session_id: str) -> DjStripeCheckoutSession:
    stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY

    stripe_res = stripe.checkout.Session.retrieve(
        session_id, expand=["customer", "payment_intent", "line_items"]
    )
    # sync djstripe model from response, then return djstripe model to be serialized
    session = DjStripeCheckoutSession.sync_from_stripe_data(stripe_res)
    session.display_items = stripe_res.line_items.data
    session.save()
    return session


def sync_stripe_customer_by_id(stripe_customer_id: str) -> DjStripeCustomer:
    stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY

    stripe_res = stripe.Customer.retrieve(stripe_customer_id)
    return DjStripeCustomer.sync_from_stripe_data(stripe_res)


def create_stripe_checkout_session(request: HttpRequest, product: Product, email: str):
    """
    Attempt to create a Stripe checkout session for product_name

    """
    stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY
    django_session_key = request.session._get_or_create_session_key()  # type: ignore[attr-defined]

    # prices = stripe.Price.list(lookup_keys=[stripe_lookup_key])

    # try to get Stripe customer from user
    user = None
    customer = None
    order_id = uuid4()

    # add django session key to stripe metadata
    extra_kwargs: Dict[Any, Any] = dict(
        # expand customer and payment_intent fields in response
        expand=["customer", "payment_intent", "line_items"],
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

    # set success / cancel urls
    extra_kwargs["success_url"] = request.build_absolute_uri("/shop/thank-you/")
    # add "{CHECKOUT_SESSION_ID}" template string to url. this gets uri-encoded to %7B if passed to build_absolute_uri fn
    extra_kwargs["success_url"] = extra_kwargs["success_url"] + "{CHECKOUT_SESSION_ID}"

    extra_kwargs["cancel_url"] = request.build_absolute_uri(f"/shop/{product.slug}")

    # quick hack to replace :8000 server-side port with front-end hot module reload port (in dev mode)
    if settings.DEBUG:
        extra_kwargs["success_url"] = extra_kwargs["success_url"].replace(
            ":8000", ":3000"
        )
        extra_kwargs["cancel_url"] = extra_kwargs["success_url"].replace(
            ":8000", ":3000"
        )
    price_id = product.prices.filter(active=True).first().id

    if product.is_shippable:

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
    elif product.is_subscription:

        return (
            stripe.checkout.Session.create(
                payment_method_types=["card"],
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
                mode="subscription",
                billing_address_collection="required",
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
        email=email,
    )
    # associate product with order
    order.products.add(product)
    # add stripe checkout redirect url to payload
    order.stripe_checkout_redirect_url = checkout_session_redirect

    # create order status
    OrderStatus.objects.create(
        order=order, status=OrderStatusType.CHECKOUT_SESSION_CREATED
    )
    return order


def sync_stripe_payment_intent(payment_intent_id: str) -> DjStripePaymentIntent:
    stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY

    stripe_res = stripe.PaymentIntent.retrieve(payment_intent_id)
    payment_intent = DjStripePaymentIntent.sync_from_stripe_data(stripe_res)
    for charge in stripe_res.charges.data:
        DjStripeCharge.sync_from_stripe_data(charge)
    payment_intent.refresh_from_db()
    return payment_intent


def sync_stripe_order(stripe_checkout_session_id) -> Order:
    """
    Sync Djstripe models associated with Stripe checkout session id
    Used to pull model data in situations where Stripe webhook events might not have arrived or settled yet
    For example, showing order confirmation page
    """
    # pull latest checkout session data from Stripe and sync DjStripe model
    session = sync_stripe_checkout_session(stripe_checkout_session_id)
    # pull latest customer info from Stripe
    customer = sync_stripe_customer_by_id(session.customer.id)
    order = Order.objects.get(djstripe_checkout_session=session)

    # if order was a payment, sync the payment intent model
    if session.mode == "payment":
        # pull latest payment intent data from Stripe
        payment_intent = sync_stripe_payment_intent(session.payment_intent.id)
        order.payment_intent = payment_intent

    order.djstripe_customer = customer

    order.save()
    return order
