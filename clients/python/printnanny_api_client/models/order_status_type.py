from enum import Enum


class OrderStatusType(str, Enum):
    CHECKOUT_SESSION_CREATED = "checkout_session_created"
    CHECKOUT_SESSION_COMPLETED = "checkout_session_completed"
    CHECKOUT_SESSION_EXPIRED = "checkout_session_expired"
    PROCESSING = "processing"
    READY_TO_SHIP = "ready_to_ship"
    SHIPPED = "shipped"
    GOODS_FULFILLED = "goods_fulfilled"
    SERVICE_FULFILLED = "service_fulfilled"
    REFUND_REQUESTED = "refund_requested"
    REFUND_GRANTED = "refund_granted"

    def __str__(self) -> str:
        return str(self.value)
