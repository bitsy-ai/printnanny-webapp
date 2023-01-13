from enum import Enum


class StripeSessionBillingAddressCollection(str, Enum):
    AUTO = "auto"
    REQUIRED = "required"

    def __str__(self) -> str:
        return str(self.value)
