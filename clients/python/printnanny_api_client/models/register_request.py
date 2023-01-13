from typing import Any, Dict, List, Type, TypeVar

import attr

from ..types import Unset

T = TypeVar("T", bound="RegisterRequest")


@attr.s(auto_attribs=True)
class RegisterRequest:
    """
    Attributes:
        email (str):
        password1 (str):
        password2 (str):
    """

    email: str
    password1: str
    password2: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        password1 = self.password1
        password2 = self.password2

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "password1": password1,
                "password2": password2,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        email = self.email if isinstance(self.email, Unset) else (None, str(self.email).encode(), "text/plain")
        password1 = (
            self.password1 if isinstance(self.password1, Unset) else (None, str(self.password1).encode(), "text/plain")
        )
        password2 = (
            self.password2 if isinstance(self.password2, Unset) else (None, str(self.password2).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "email": email,
                "password1": password1,
                "password2": password2,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email")

        password1 = d.pop("password1")

        password2 = d.pop("password2")

        register_request = cls(
            email=email,
            password1=password1,
            password2=password2,
        )

        register_request.additional_properties = d
        return register_request

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
