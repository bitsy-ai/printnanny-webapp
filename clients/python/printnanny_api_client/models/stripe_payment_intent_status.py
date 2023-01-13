from enum import Enum


class StripePaymentIntentStatus(str, Enum):
    CANCELED = "canceled"
    PROCESSING = "processing"
    REQUIRES_ACTION = "requires_action"
    REQUIRES_CAPTURE = "requires_capture"
    REQUIRES_CONFIRMATION = "requires_confirmation"
    REQUIRES_PAYMENT_METHOD = "requires_payment_method"
    SUCCEEDED = "succeeded"

    def __str__(self) -> str:
        return str(self.value)
