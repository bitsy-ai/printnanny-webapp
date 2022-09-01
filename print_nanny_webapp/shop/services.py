from django.conf import settings
from django.http.request import HttpRequest

from djstripe.models.checkout import Session
from djstripe.models import Customer
from djstripe.settings import djstripe_settings

import stripe


def sync_stripe_checkout_session(session_id: str) -> Session:
    stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY

    stripe_res = stripe.checkout.Session.retrieve(session_id)
    # sync djstripe model from response, then return djstripe model to be serialized
    return Session.sync_from_stripe_data(stripe_res)


def sync_stripe_customer_by_id(stripe_customer_id: str) -> Customer:
    stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY

    stripe_res = stripe.Customer.retrieve(stripe_customer_id)
    return Customer.sync_from_stripe_data(stripe_res)


def create_stripe_checkout_session(
    request: HttpRequest,
    stripe_lookup_key: str,
    django_session_key: str,
):
    """
    Attempt to create a Stripe checkout session for product_name

    """
    stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY

    prices = stripe.Price.list(lookup_keys=[stripe_lookup_key])

    # try to get Stripe customer from user
    user = None
    customer = None

    if request.user.is_authenticated:
        user = request.user

    # add django session key to stripe metadata
    extra_kwargs = dict(metadata=dict(django_session_key=django_session_key))

    if user is not None:
        # provides djstripe_subscriber_user reverse relationship
        extra_kwargs["metadata"][djstripe_settings.SUBSCRIBER_CUSTOMER_KEY] = user.id
        # an extra reference id
        extra_kwargs["client_reference_id"] = user.id
        try:
            customer = Customer.objects.get(subscriber=user)
            extra_kwargs["customer"] = customer.id

        # customer not found
        except Customer.DoesNotExist:
            pass

    if stripe_lookup_key == "sdwire_preorder":
        if len(prices.data) > 1:
            raise ValueError(
                f"stripe.Price.list returned {len(prices)} prices for lookup_key {stripe_lookup_key} (expected 1): {prices.data}"
            )
        price_id = prices.data[0].id

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

        return stripe.checkout.Session.create(
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
        )
    raise NotImplementedError(
        f"create_stripe_checkout_session not implemented for stripe_lookup_key={stripe_lookup_key}"
    )
