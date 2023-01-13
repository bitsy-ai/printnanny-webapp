from enum import Enum


class StripeSessionMode(str, Enum):
    PAYMENT = "payment"
    SETUP = "setup"
    SUBSCRIPTION = "subscription"

    def __str__(self) -> str:
        return str(self.value)
