from django.db import models


class OrderStatusType(models.TextChoices):
    CHECKOUT_SESSION_CREATED = ("checkout_session_created", "Checkout session created")
    CHECKOUT_SESSION_COMPLETED = (
        "checkout_session_completed",
        "Checkout session completed",
    )
    CHECKOUT_SESSION_EXPIRED = (
        "checkout_session_expired",
        "Checkout session expired",
    )
    PAYMENT_INTENT = (
        "checkout_session_success",
        "Added PaymentIntent to checkout session",
    )

    PROCESSING = ("processing", "Order is being proccessed")
    READY_TO_SHIP = ("ready_to_ship", "Order is ready to ship")
    SHIPPED = ("shipped", "Order has been passed shipping service")
    GOODS_FULFILLED = ("goods_fulfilled", "Physical goods order fulfilled")
    SERVICE_FULFILLED = (
        "service_fulfilled",
        "Electronic service or subscription fulfilled",
    )
    REFUND_REQUESTED = ("refund_requested", "Refund requested")
    REFUND_GRANTED = ("refund_granted", "Refund granted")


class ReferralCodeType(models.TextChoices):
    FOUNDING_MEMBER_TRIAL = (
        "founding_member_trial",
        "A Founding Member has invited you to try PrintNanny",
    )
