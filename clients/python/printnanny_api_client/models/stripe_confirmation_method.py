from enum import Enum


class StripeConfirmationMethod(str, Enum):
    AUTOMATIC = "automatic"
    MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
