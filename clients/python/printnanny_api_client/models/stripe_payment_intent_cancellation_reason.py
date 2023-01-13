from enum import Enum


class StripePaymentIntentCancellationReason(str, Enum):
    ABANDONED = "abandoned"
    AUTOMATIC = "automatic"
    DUPLICATE = "duplicate"
    FAILED_INVOICE = "failed_invoice"
    FRAUDULENT = "fraudulent"
    REQUESTED_BY_CUSTOMER = "requested_by_customer"
    VOID_INVOICE = "void_invoice"

    def __str__(self) -> str:
        return str(self.value)
