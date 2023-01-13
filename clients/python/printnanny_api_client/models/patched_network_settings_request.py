from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.preferred_dns_type import PreferredDnsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedNetworkSettingsRequest")


@attr.s(auto_attribs=True)
class PatchedNetworkSettingsRequest:
    """
    Attributes:
        preferred_dns (Union[Unset, PreferredDnsType]):
        user (Union[Unset, int]):
    """

    preferred_dns: Union[Unset, PreferredDnsType] = UNSET
    user: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        preferred_dns: Union[Unset, str] = UNSET
        if not isinstance(self.preferred_dns, Unset):
            preferred_dns = self.preferred_dns.value

        user = self.user

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if preferred_dns is not UNSET:
            field_dict["preferred_dns"] = preferred_dns
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        preferred_dns: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.preferred_dns, Unset):
            preferred_dns = (None, str(self.preferred_dns.value).encode(), "text/plain")

        user = self.user if isinstance(self.user, Unset) else (None, str(self.user).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if preferred_dns is not UNSET:
            field_dict["preferred_dns"] = preferred_dns
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _preferred_dns = d.pop("preferred_dns", UNSET)
        preferred_dns: Union[Unset, PreferredDnsType]
        if isinstance(_preferred_dns, Unset):
            preferred_dns = UNSET
        else:
            preferred_dns = PreferredDnsType(_preferred_dns)

        user = d.pop("user", UNSET)

        patched_network_settings_request = cls(
            preferred_dns=preferred_dns,
            user=user,
        )

        patched_network_settings_request.additional_properties = d
        return patched_network_settings_request

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
