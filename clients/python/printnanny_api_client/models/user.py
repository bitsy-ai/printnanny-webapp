from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@attr.s(auto_attribs=True)
class User:
    """
    Attributes:
        email (str):
        id (int):
        is_beta_tester (bool):
        first_name (Union[Unset, None, str]):
        last_name (Union[Unset, None, str]):
    """

    email: str
    id: int
    is_beta_tester: bool
    first_name: Union[Unset, None, str] = UNSET
    last_name: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        id = self.id
        is_beta_tester = self.is_beta_tester
        first_name = self.first_name
        last_name = self.last_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "id": id,
                "is_beta_tester": is_beta_tester,
            }
        )
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email")

        id = d.pop("id")

        is_beta_tester = d.pop("is_beta_tester")

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        user = cls(
            email=email,
            id=id,
            is_beta_tester=is_beta_tester,
            first_name=first_name,
            last_name=last_name,
        )

        user.additional_properties = d
        return user

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
