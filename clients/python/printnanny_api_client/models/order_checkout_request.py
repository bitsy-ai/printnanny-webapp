import json
from typing import Any, Dict, List, Type, TypeVar, cast

import attr

from ..types import Unset

T = TypeVar("T", bound="OrderCheckoutRequest")


@attr.s(auto_attribs=True)
class OrderCheckoutRequest:
    """
    Attributes:
        products (List[str]):
        email (str):
    """

    products: List[str]
    email: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        products = self.products

        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "products": products,
                "email": email,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        _temp_products = self.products
        products = (None, json.dumps(_temp_products).encode(), "application/json")

        email = self.email if isinstance(self.email, Unset) else (None, str(self.email).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "products": products,
                "email": email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        products = cast(List[str], d.pop("products"))

        email = d.pop("email")

        order_checkout_request = cls(
            products=products,
            email=email,
        )

        order_checkout_request.additional_properties = d
        return order_checkout_request

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
