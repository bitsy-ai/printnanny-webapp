from uuid import uuid4
from typing import Dict, Any
from django.http import HttpRequest
from django.contrib.auth import get_user_model

from djstripe.models.core import (
    Customer as DjStripeCustomer,
    PaymentIntent as DjStripePaymentIntent,
    Charge as DjStripeCharge,
    Price as DjStripePrice,
)
from djstripe.models import Subscription as DjStripeSubscription
from djstripe.settings import djstripe_settings
from djstripe.models.checkout import Session as DjStripeCheckoutSession


import stripe

from print_nanny_webapp.shop.models import OrderStatus, Product, Order
from print_nanny_webapp.shop.enum import OrderStatusType
from print_nanny_webapp.users.services import get_or_create_user_by_email

User = get_user_model()


def sync_stripe_checkout_session(session_id: str) -> DjStripeCheckoutSession:
    stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY

    stripe_res = stripe.checkout.Session.retrieve(
        session_id, expand=["customer", "payment_intent", "line_items", "subscription"]
    )
    # sync djstripe model from response, then return djstripe model to be serialized
    session = DjStripeCheckoutSession.sync_from_stripe_data(stripe_res)
    session.display_items = stripe_res.line_items.data
    session.save()
    return session


def sync_stripe_customer_by_id(stripe_customer_id: str) -> DjStripeCustomer:
    stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY

    stripe_res = stripe.Customer.retrieve(stripe_customer_id)
    customer = DjStripeCustomer.sync_from_stripe_data(stripe_res)
    customer.save()
    return customer


def build_stripe_checkout_session_kwargs_v1(
    request: HttpRequest, email: str, order_id: str, price_id: str, product: Product
) -> Dict[Any, Any]:
    """
    Looks up customer (by email) to associate Stripe Checkout Session with an existing customer

    If Customer doesn't exist, set Stripe API kwargs needed to create Stripe Customer during Stripe Checkout Session flow
    """
    # get or create user by email address
    user = get_or_create_user_by_email(email)
    # add django session key to stripe metadata
    django_session_key = request.session._get_or_create_session_key()  # type: ignore[attr-defined]
    extra_kwargs: Dict[Any, Any] = dict(
        # expand customer and payment_intent fields in response
        expand=["customer", "payment_intent", "line_items"],
        metadata=dict(
            django_session_key=django_session_key,
            django_product_id=product.id,
            django_order_id=order_id,
        ),
        allow_promotion_codes=True,
    )
    # set success / cancel urls
    extra_kwargs["success_url"] = request.build_absolute_uri("/shop/thank-you/")
    # add "{CHECKOUT_SESSION_ID}" template string to url. this gets uri-encoded to %7B if passed to build_absolute_uri fn
    extra_kwargs["success_url"] = extra_kwargs["success_url"] + "{CHECKOUT_SESSION_ID}"
    extra_kwargs["cancel_url"] = request.build_absolute_uri(f"/shop/{product.slug}")

    extra_kwargs["client_reference_id"] = user.id
    try:
        customer = DjStripeCustomer.objects.get(subscriber=user)
        extra_kwargs["customer"] = customer.id
        # automatically update Stripe customer with shipping/billing address if these fields are modified during checkout session
        extra_kwargs["customer_update"] = dict(
            name="auto", shipping="auto", address="auto"
        )
        extra_kwargs["metadata"][
            djstripe_settings.SUBSCRIBER_CUSTOMER_KEY
        ] = customer.subscriber.id
    # customer not found - pass email to Stripe Checkout Session create call
    # Django User creation will be handled in Stripe Checkout Session redirect
    except DjStripeCustomer.DoesNotExist:
        extra_kwargs["customer_email"] = email

        if product.is_subscription is False:
            # in subscription mode, Stripe always creates a Customer object (by default)
            # in payment mode, we must set customer_creation to "always"
            # see: https://stripe.com/docs/api/checkout/sessions/create#create_checkout_session-customer_creation
            extra_kwargs["customer_creation"] = "always"

    else:
        try:
            customer = DjStripeCustomer.objects.get(email=email)
            extra_kwargs["customer"] = customer.id
            extra_kwargs["client_reference_id"] = customer.subscriber.id
            extra_kwargs["metadata"][
                djstripe_settings.SUBSCRIBER_CUSTOMER_KEY
            ] = customer.subscriber.id
        # customer not found - pass email to Stripe Checkout Session create call
        # Django User creation will be handled in Stripe Checkout Session redirect
        except DjStripeCustomer.DoesNotExist:
            extra_kwargs["customer_email"] = email
            if product.is_subscription is False:
                # in subscription mode, Stripe always creates a Customer object (by default)
                # in payment mode, we must set customer_creation to "always"
                # see: https://stripe.com/docs/api/checkout/sessions/create#create_checkout_session-customer_creation
                extra_kwargs["customer_creation"] = "always"
    # end Stripe Customer kwargs

    if product.is_shippable:
        payment_kwargs = dict(
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
            automatic_tax={
                "enabled": True,
            },
            tax_id_collection={
                "enabled": True,
            },
            shipping_options=[
                {
                    "shipping_rate_data": {
                        "type": "fixed_amount",
                        "fixed_amount": {
                            "amount": 999,
                            "currency": "usd",
                        },
                        "display_name": "USPS Ground",
                        # Stripe will automatically determine if shipping is a taxable (varies by state/country), then calculate correct tax
                        # See: https://stripe.com/docs/payments/checkout/shipping#shipping-rate-with-tax-code
                        "tax_code": "txcd_92010001",
                        "tax_behavior": "exclusive",
                    }
                },
            ],
        )
    elif product.is_subscription:
        payment_kwargs = dict(
            payment_method_types=["card"],
            line_items=[
                {
                    "price": price_id,
                    "quantity": 1,
                }
            ],
            automatic_tax={
                "enabled": True,
            },
            tax_id_collection={
                "enabled": True,
            },
            mode="subscription",
            billing_address_collection="required",
        )
    else:
        raise NotImplementedError(
            f"create_stripe_checkout_session not implemented for Products={product}"
        )
    extra_kwargs.update(payment_kwargs)
    return extra_kwargs


def create_stripe_checkout_session(
    request: HttpRequest, product: Product, price_id: str, email: str
):
    """
    Attempt to create a Stripe checkout session for product_name

    """
    stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY

    # prices = stripe.Price.list(lookup_keys=[stripe_lookup_key])

    order_id = uuid4()

    # try to get Stripe customer from Django user authentication, email lookup, or supply needed parameters to create new Stripe Customer
    extra_kwargs = build_stripe_checkout_session_kwargs_v1(
        request, email, str(order_id), price_id, product
    )

    return (
        stripe.checkout.Session.create(
            **extra_kwargs,
        ),
        order_id,
    )


def create_order(request: HttpRequest, product: Product, price_id: str, email: str):
    checkout_session_res, order_id = create_stripe_checkout_session(
        request, product, price_id, email
    )
    checkout_session_redirect = checkout_session_res.url
    checkout_session = DjStripeCheckoutSession.sync_from_stripe_data(
        checkout_session_res
    )
    checkout_session.save()
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
    order.stripe_checkout_session_id = checkout_session.id

    # create order status
    OrderStatus.objects.create(
        order=order, status=OrderStatusType.CHECKOUT_SESSION_CREATED
    )
    return order


def sync_stripe_payment_intent(payment_intent_id: str) -> DjStripePaymentIntent:
    stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY

    stripe_res = stripe.PaymentIntent.retrieve(payment_intent_id)
    payment_intent = DjStripePaymentIntent.sync_from_stripe_data(stripe_res)
    payment_intent.save()
    for charge in stripe_res.charges.data:
        charge_obj = DjStripeCharge.sync_from_stripe_data(charge)
        charge_obj.save()
    payment_intent.refresh_from_db()
    return payment_intent


def sync_stripe_subscription(subscription_id: str) -> DjStripeSubscription:
    stripe_res = stripe.Subscription.retrieve(subscription_id)
    subscription = DjStripeSubscription.sync_from_stripe_data(stripe_res)
    subscription.save()
    return subscription


def sync_stripe_order(stripe_checkout_session_id) -> Order:
    """
    Sync Djstripe models associated with Stripe checkout session id
    Used to pull model data in situations where Stripe webhook events might not have arrived or settled yet
    For example, showing order confirmation page
    """
    # pull latest checkout session data from Stripe and sync DjStripe model
    session = sync_stripe_checkout_session(stripe_checkout_session_id)
    # pull latest customer info from Stripe
    if session.customer is None:
        # get Stripe Customer id by email
        stripe_customer_data = stripe.Customer.search(
            query=f"email:'{session.customer_email}'", limit=1
        )
        # import pdb

        # pdb.set_trace()
        if (
            len(stripe_customer_data.data) == 1
            and stripe_customer_data.data[0].get("id") is not None
        ):
            customer_id = stripe_customer_data.data.get("id")
            customer = sync_stripe_customer_by_id(customer_id)
        else:
            raise ValueError(
                "Something went wrong processing your payment, please email support@printnanny.ai for help."
            )
    else:
        customer = sync_stripe_customer_by_id(session.customer.id)
    order = Order.objects.get(djstripe_checkout_session=session)

    # if order was a payment, sync the payment intent model
    if session.mode == "payment":
        # pull latest payment intent data from Stripe
        payment_intent = sync_stripe_payment_intent(session.payment_intent.id)
        order.djstripe_payment_intent = payment_intent
        payment_intent.save()

    # if order was a subscription, sync the subscription models
    elif session.mode == "subscription":
        subscription = sync_stripe_subscription(session.subscription.id)
        order.djstripe_subscription = subscription
        subscription.save()

    order.djstripe_customer = customer

    # if order.user is None, attempt to reconcile with existing user by email
    if order.user is None:
        try:
            user = User.objects.get(email=order.email)  # type: ignore[has-type]
            order.user = user
        except User.DoesNotExist:
            # user will be prompted to create a password in checkout view
            pass

    order.save()
    return order
