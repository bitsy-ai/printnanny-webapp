from typing import Any, Dict, List, Type, TypeVar

import attr

from ..types import Unset

T = TypeVar("T", bound="PasswordResetConfirmRequest")


@attr.s(auto_attribs=True)
class PasswordResetConfirmRequest:
    """Serializer for confirming a password reset attempt.

    Attributes:
        new_password1 (str):
        new_password2 (str):
        uid (str):
        token (str):
    """

    new_password1: str
    new_password2: str
    uid: str
    token: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        new_password1 = self.new_password1
        new_password2 = self.new_password2
        uid = self.uid
        token = self.token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "new_password1": new_password1,
                "new_password2": new_password2,
                "uid": uid,
                "token": token,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        new_password1 = (
            self.new_password1
            if isinstance(self.new_password1, Unset)
            else (None, str(self.new_password1).encode(), "text/plain")
        )
        new_password2 = (
            self.new_password2
            if isinstance(self.new_password2, Unset)
            else (None, str(self.new_password2).encode(), "text/plain")
        )
        uid = self.uid if isinstance(self.uid, Unset) else (None, str(self.uid).encode(), "text/plain")
        token = self.token if isinstance(self.token, Unset) else (None, str(self.token).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "new_password1": new_password1,
                "new_password2": new_password2,
                "uid": uid,
                "token": token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        new_password1 = d.pop("new_password1")

        new_password2 = d.pop("new_password2")

        uid = d.pop("uid")

        token = d.pop("token")

        password_reset_confirm_request = cls(
            new_password1=new_password1,
            new_password2=new_password2,
            uid=uid,
            token=token,
        )

        password_reset_confirm_request.additional_properties = d
        return password_reset_confirm_request

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
