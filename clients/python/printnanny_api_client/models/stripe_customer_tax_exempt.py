from enum import Enum


class StripeCustomerTaxExempt(str, Enum):
    EXEMPT = "exempt"
    NONE = "none"
    REVERSE = "reverse"

    def __str__(self) -> str:
        return str(self.value)
