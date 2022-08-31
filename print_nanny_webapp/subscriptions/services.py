import logging
from typing import Optional
from django.contrib.auth import get_user_model
from djstripe.settings import djstripe_settings
from djstripe.models import Customer, Subscription, Invoice, Charge, Event
import stripe


logger = logging.getLogger(__name__)

User = get_user_model()


def create_stripe_checkout_session(
    stripe_lookup_key: str, django_session_key: str, user: Optional[User] = None
):
    """
    Attempt to create a Stripe checkout session for product_name

    """
    stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY
    prices = stripe.Price.list(lookup_keys=[stripe_lookup_key])

    # try to get Stripe customer from user
    customer = None
    extra_kwargs = dict(metadata=dict(django_session_key=django_session_key))
    if user is not None:
        # provides djstripe_subscriber_user reverse relationship
        extra_kwargs["metadata"][
            djstripe_settings.djstripe_settings.SUBSCRIBER_CUSTOMER_KEY
        ] = user.id
        # an extra reference id
        extra_kwargs["client_reference_id"] = user.id
        try:
            customer = Customer.objects.get(subscriber=user)
            extra_kwargs["customer"] = customer.id
            extra_kwargs["customer_email"] = customer.email

        # customer not found
        except Customer.DoesNotExist:
            pass

    if stripe_lookup_key == "sdwire_preorder":
        if len(prices.data) > 1:
            raise ValueError(
                f"stripe.Price.list returned {len(prices)} prices for lookup_key {stripe_lookup_key} (expected 1): {prices.data}"
            )
        price_id = prices.data[0].id
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
            success_url="https://printnanny.ai/shop/checkout/success",
            cancel_url="https://printnanny.ai/shop/sdwire",
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
