from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.preferred_dns_type import PreferredDnsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="NetworkSettingsRequest")


@attr.s(auto_attribs=True)
class NetworkSettingsRequest:
    """
    Attributes:
        user (int):
        preferred_dns (Union[Unset, PreferredDnsType]):
    """

    user: int
    preferred_dns: Union[Unset, PreferredDnsType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user = self.user
        preferred_dns: Union[Unset, str] = UNSET
        if not isinstance(self.preferred_dns, Unset):
            preferred_dns = self.preferred_dns.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
            }
        )
        if preferred_dns is not UNSET:
            field_dict["preferred_dns"] = preferred_dns

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        user = self.user if isinstance(self.user, Unset) else (None, str(self.user).encode(), "text/plain")
        preferred_dns: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.preferred_dns, Unset):
            preferred_dns = (None, str(self.preferred_dns.value).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "user": user,
            }
        )
        if preferred_dns is not UNSET:
            field_dict["preferred_dns"] = preferred_dns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user = d.pop("user")

        _preferred_dns = d.pop("preferred_dns", UNSET)
        preferred_dns: Union[Unset, PreferredDnsType]
        if isinstance(_preferred_dns, Unset):
            preferred_dns = UNSET
        else:
            preferred_dns = PreferredDnsType(_preferred_dns)

        network_settings_request = cls(
            user=user,
            preferred_dns=preferred_dns,
        )

        network_settings_request.additional_properties = d
        return network_settings_request

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
