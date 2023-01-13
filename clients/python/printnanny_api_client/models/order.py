import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dj_stripe_checkout_session import DjStripeCheckoutSession
    from ..models.dj_stripe_customer import DjStripeCustomer
    from ..models.dj_stripe_payment_intent import DjStripePaymentIntent
    from ..models.order_status import OrderStatus
    from ..models.order_stripe_checkout_session_data import OrderStripeCheckoutSessionData
    from ..models.product import Product
    from ..models.user import User


T = TypeVar("T", bound="Order")


@attr.s(auto_attribs=True)
class Order:
    """Djstripe's representation of Stripe Checkout model is missing a number of fields, like subtotal amount and
    shipping/tax charges

    stripe_checkout_session_data is the raw JSON returned by stripe.checkout.Session.retrieve

        Attributes:
            created_dt (datetime.datetime):
            djstripe_checkout_session (DjStripeCheckoutSession):
            djstripe_customer (DjStripeCustomer):
            djstripe_payment_intent (DjStripePaymentIntent):
            email (str):
            id (str):
            is_shippable (bool):
            is_subscription (bool):
            last_status (OrderStatus):
            products (List['Product']):
            status_history (List['OrderStatus']):
            stripe_checkout_redirect_url (str):
            stripe_checkout_session_data (OrderStripeCheckoutSessionData):
            user (Union[Unset, User]):
            receipt_url (Optional[str]):
            portal_url (Optional[str]):
    """

    created_dt: datetime.datetime
    djstripe_checkout_session: "DjStripeCheckoutSession"
    djstripe_customer: "DjStripeCustomer"
    djstripe_payment_intent: "DjStripePaymentIntent"
    email: str
    id: str
    is_shippable: bool
    is_subscription: bool
    last_status: "OrderStatus"
    products: List["Product"]
    status_history: List["OrderStatus"]
    stripe_checkout_redirect_url: str
    stripe_checkout_session_data: "OrderStripeCheckoutSessionData"
    receipt_url: Optional[str]
    portal_url: Optional[str]
    user: Union[Unset, "User"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_dt = self.created_dt.isoformat()

        djstripe_checkout_session = self.djstripe_checkout_session.to_dict()

        djstripe_customer = self.djstripe_customer.to_dict()

        djstripe_payment_intent = self.djstripe_payment_intent.to_dict()

        email = self.email
        id = self.id
        is_shippable = self.is_shippable
        is_subscription = self.is_subscription
        last_status = self.last_status.to_dict()

        products = []
        for products_item_data in self.products:
            products_item = products_item_data.to_dict()

            products.append(products_item)

        status_history = []
        for status_history_item_data in self.status_history:
            status_history_item = status_history_item_data.to_dict()

            status_history.append(status_history_item)

        stripe_checkout_redirect_url = self.stripe_checkout_redirect_url
        stripe_checkout_session_data = self.stripe_checkout_session_data.to_dict()

        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        receipt_url = self.receipt_url
        portal_url = self.portal_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_dt": created_dt,
                "djstripe_checkout_session": djstripe_checkout_session,
                "djstripe_customer": djstripe_customer,
                "djstripe_payment_intent": djstripe_payment_intent,
                "email": email,
                "id": id,
                "is_shippable": is_shippable,
                "is_subscription": is_subscription,
                "last_status": last_status,
                "products": products,
                "status_history": status_history,
                "stripe_checkout_redirect_url": stripe_checkout_redirect_url,
                "stripe_checkout_session_data": stripe_checkout_session_data,
                "receipt_url": receipt_url,
                "portal_url": portal_url,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dj_stripe_checkout_session import DjStripeCheckoutSession
        from ..models.dj_stripe_customer import DjStripeCustomer
        from ..models.dj_stripe_payment_intent import DjStripePaymentIntent
        from ..models.order_status import OrderStatus
        from ..models.order_stripe_checkout_session_data import OrderStripeCheckoutSessionData
        from ..models.product import Product
        from ..models.user import User

        d = src_dict.copy()
        created_dt = isoparse(d.pop("created_dt"))

        djstripe_checkout_session = DjStripeCheckoutSession.from_dict(d.pop("djstripe_checkout_session"))

        djstripe_customer = DjStripeCustomer.from_dict(d.pop("djstripe_customer"))

        djstripe_payment_intent = DjStripePaymentIntent.from_dict(d.pop("djstripe_payment_intent"))

        email = d.pop("email")

        id = d.pop("id")

        is_shippable = d.pop("is_shippable")

        is_subscription = d.pop("is_subscription")

        last_status = OrderStatus.from_dict(d.pop("last_status"))

        products = []
        _products = d.pop("products")
        for products_item_data in _products:
            products_item = Product.from_dict(products_item_data)

            products.append(products_item)

        status_history = []
        _status_history = d.pop("status_history")
        for status_history_item_data in _status_history:
            status_history_item = OrderStatus.from_dict(status_history_item_data)

            status_history.append(status_history_item)

        stripe_checkout_redirect_url = d.pop("stripe_checkout_redirect_url")

        stripe_checkout_session_data = OrderStripeCheckoutSessionData.from_dict(d.pop("stripe_checkout_session_data"))

        _user = d.pop("user", UNSET)
        user: Union[Unset, User]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)

        receipt_url = d.pop("receipt_url")

        portal_url = d.pop("portal_url")

        order = cls(
            created_dt=created_dt,
            djstripe_checkout_session=djstripe_checkout_session,
            djstripe_customer=djstripe_customer,
            djstripe_payment_intent=djstripe_payment_intent,
            email=email,
            id=id,
            is_shippable=is_shippable,
            is_subscription=is_subscription,
            last_status=last_status,
            products=products,
            status_history=status_history,
            stripe_checkout_redirect_url=stripe_checkout_redirect_url,
            stripe_checkout_session_data=stripe_checkout_session_data,
            user=user,
            receipt_url=receipt_url,
            portal_url=portal_url,
        )

        order.additional_properties = d
        return order

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
