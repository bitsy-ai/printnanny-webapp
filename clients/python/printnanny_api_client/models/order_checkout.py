from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="OrderCheckout")


@attr.s(auto_attribs=True)
class OrderCheckout:
    """
    Attributes:
        products (List[str]):
        email (str):
        stripe_checkout_redirect_url (str):
        stripe_checkout_session_id (str):
    """

    products: List[str]
    email: str
    stripe_checkout_redirect_url: str
    stripe_checkout_session_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        products = self.products

        email = self.email
        stripe_checkout_redirect_url = self.stripe_checkout_redirect_url
        stripe_checkout_session_id = self.stripe_checkout_session_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "products": products,
                "email": email,
                "stripe_checkout_redirect_url": stripe_checkout_redirect_url,
                "stripe_checkout_session_id": stripe_checkout_session_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        products = cast(List[str], d.pop("products"))

        email = d.pop("email")

        stripe_checkout_redirect_url = d.pop("stripe_checkout_redirect_url")

        stripe_checkout_session_id = d.pop("stripe_checkout_session_id")

        order_checkout = cls(
            products=products,
            email=email,
            stripe_checkout_redirect_url=stripe_checkout_redirect_url,
            stripe_checkout_session_id=stripe_checkout_session_id,
        )

        order_checkout.additional_properties = d
        return order_checkout

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
