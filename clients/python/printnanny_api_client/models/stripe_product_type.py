from enum import Enum


class StripeProductType(str, Enum):
    GOOD = "good"
    SERVICE = "service"

    def __str__(self) -> str:
        return str(self.value)
