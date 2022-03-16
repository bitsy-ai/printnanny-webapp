import logging
from typing import Optional
from django.db.models import Q
from djstripe.settings import djstripe_settings
from djstripe.models import Customer, Subscription, Charge, Event, Invoice, InvoiceItem
import stripe

from print_nanny_webapp.users.models import User

logger = logging.getLogger(__name__)


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


def get_stripe_active_subscription(customer: Customer) -> Subscription:
    subscriptions = customer.subscriptions.all().order_by("-created")
    return subscriptions.first()


def get_stripe_customer(user: User) -> Customer:
    """
    Retrieve djstripe.model.Customer where Customer <-> User relationship may not be set
    Sets Customer.subscriber relationship if unset
    """
    query = Q(subscriber=user) | Q(email=user.email)
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
