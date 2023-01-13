import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.preferred_dns_type import PreferredDnsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="NetworkSettings")


@attr.s(auto_attribs=True)
class NetworkSettings:
    """
    Attributes:
        id (int):
        updated_dt (datetime.datetime):
        user (int):
        preferred_dns (Union[Unset, PreferredDnsType]):
    """

    id: int
    updated_dt: datetime.datetime
    user: int
    preferred_dns: Union[Unset, PreferredDnsType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        updated_dt = self.updated_dt.isoformat()

        user = self.user
        preferred_dns: Union[Unset, str] = UNSET
        if not isinstance(self.preferred_dns, Unset):
            preferred_dns = self.preferred_dns.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "updated_dt": updated_dt,
                "user": user,
            }
        )
        if preferred_dns is not UNSET:
            field_dict["preferred_dns"] = preferred_dns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        updated_dt = isoparse(d.pop("updated_dt"))

        user = d.pop("user")

        _preferred_dns = d.pop("preferred_dns", UNSET)
        preferred_dns: Union[Unset, PreferredDnsType]
        if isinstance(_preferred_dns, Unset):
            preferred_dns = UNSET
        else:
            preferred_dns = PreferredDnsType(_preferred_dns)

        network_settings = cls(
            id=id,
            updated_dt=updated_dt,
            user=user,
            preferred_dns=preferred_dns,
        )

        network_settings.additional_properties = d
        return network_settings

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
