from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CallbackTokenAuthRequest")


@attr.s(auto_attribs=True)
class CallbackTokenAuthRequest:
    """Abstract class inspired by DRF's own token serializer.
    Returns a user if valid, None or a message if not.

        Attributes:
            token (str):
            email (Union[Unset, str]):
            mobile (Union[Unset, str]):
    """

    token: str
    email: Union[Unset, str] = UNSET
    mobile: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token = self.token
        email = self.email
        mobile = self.mobile

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if mobile is not UNSET:
            field_dict["mobile"] = mobile

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        token = self.token if isinstance(self.token, Unset) else (None, str(self.token).encode(), "text/plain")
        email = self.email if isinstance(self.email, Unset) else (None, str(self.email).encode(), "text/plain")
        mobile = self.mobile if isinstance(self.mobile, Unset) else (None, str(self.mobile).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "token": token,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if mobile is not UNSET:
            field_dict["mobile"] = mobile

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token")

        email = d.pop("email", UNSET)

        mobile = d.pop("mobile", UNSET)

        callback_token_auth_request = cls(
            token=token,
            email=email,
            mobile=mobile,
        )

        callback_token_auth_request.additional_properties = d
        return callback_token_auth_request

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
