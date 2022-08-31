import logging
from typing import Optional
from django.conf import settings
from django.http.request import HttpRequest
from django.contrib.auth import get_user_model
from django.db.models import Q
from djstripe.settings import djstripe_settings
from djstripe.models import Customer, Subscription, Invoice, Charge, Event
from djstripe.models.checkout import Session
import stripe


logger = logging.getLogger(__name__)

User = get_user_model()


def get_stripe_checkout_session(session_id: str) -> Session:
    stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY

    return stripe.checkout.Session.retrieve(session_id)


def get_stripe_customer_by_id(stripe_customer_id: str) -> Customer:
    stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY

    return stripe.Customer.retrieve(stripe_customer_id)


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
            "/shop/sdwire/success?session_id="
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


def link_customer_by_email(user) -> Customer:
    customer = Customer.objects.get(email=user.email, deleted=False)
    if customer.subscriber is None:
        customer.subscriber = user
        customer.save()
    elif customer.subscriber_id != user.id:
        logger.warning(
            "Tried to associate djstripe.models.Customer with email=%s with user=%s, but customer already linked to user=%s",
            customer.email,
            user,
            customer.subscriber,
        )
    return customer


def get_stripe_subscription(customer: Customer) -> Subscription:
    subscriptions = customer.subscriptions.all().order_by("-created")
    return subscriptions.first()


def get_stripe_customer(user: User) -> Customer:
    """
    Retrieve djstripe.model.Customer where Customer <-> User relationship may not be set
    Sets Customer.subscriber relationship if unset
    """
    query = Q(subscriber=user, deleted=False) | Q(email=user.email, deleted=False)
    customer = Customer.objects.get(query)
    if not customer.subscriber:
        link_customer_by_email(user)
    return customer


def get_stripe_charges(customer: Customer):
    return Charge.objects.filter(customer=customer).all().order_by("-created")


def get_stripe_invoices(customer: Customer):
    return Invoice.objects.filter(customer=customer).all().order_by("-created")


def get_stripe_subscription_events(customer: Customer):
    types = [
        "customer.created",
        "customer.deleted",
        "customer.discount.created",
        "customer.discount.deleted",
        "customer.discount.updated",
        "customer.source.created",
        "customer.source.deleted",
        "customer.source.updated",
        "customer.source.expiring",
        "customer.subscription.created",
        "customer.subscription.deleted",
        "customer.subscription.pending_update_applied",
        "customer.subscription.pending_update_expired",
        "customer.subscription.trial_will_end",
        # "customer.subscription.updated",
        "invoice.paid",
        "invoice.payment_action_required",
        "invoice.payment_failed",
        "invoice.payment_succeeded",
        "invoice.sent",
        "invoice.upcoming",
        "invoice.updated",
        "invoice.voided",
        "invoice.deleted",
        "invoice.updated",
    ]
    return (
        Event.objects.filter(
            Q(data__object__id=customer.id, type__in=types)
            | Q(data__object__customer=customer.id, type__in=types)
        )
        .all()
        .order_by("-created")
    )


def get_stripe_next_invoice(
    customer: Customer, subscription: Subscription
) -> Optional[stripe.Invoice]:
    try:
        invoice = Invoice.stripe_class.upcoming(
            api_key=djstripe_settings.STRIPE_SECRET_KEY,
            customer=customer.id,
            subscription=subscription.id,
        )
    except stripe.error.InvalidRequestError as exc:
        if str(exc) != "Nothing to invoice for customer":
            raise
        return None
    # invoice = Invoice.upcoming(customer=customer, subscription=subscription)
    logger.info("Got invoice %s", invoice)
    return invoice
