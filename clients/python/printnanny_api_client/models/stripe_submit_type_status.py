from enum import Enum


class StripeSubmitTypeStatus(str, Enum):
    AUTO = "auto"
    BOOK = "book"
    DONATE = "donate"
    PAY = "pay"

    def __str__(self) -> str:
        return str(self.value)
