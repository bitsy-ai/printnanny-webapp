from enum import Enum


class StripeSourceCodeVerificationStatus(str, Enum):
    FAILED = "failed"
    PENDING = "pending"
    SUCCEEDED = "succeeded"

    def __str__(self) -> str:
        return str(self.value)
