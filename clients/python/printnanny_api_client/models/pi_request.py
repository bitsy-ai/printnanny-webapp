from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.sbc_enum import SbcEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PiRequest")


@attr.s(auto_attribs=True)
class PiRequest:
    """
    Attributes:
        sbc (Union[Unset, SbcEnum]):
        hostname (Union[Unset, str]): Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options
            menu (without .local extension)
        favorite (Union[Unset, bool]):
        setup_finished (Union[Unset, bool]):
    """

    sbc: Union[Unset, SbcEnum] = UNSET
    hostname: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    setup_finished: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sbc: Union[Unset, str] = UNSET
        if not isinstance(self.sbc, Unset):
            sbc = self.sbc.value

        hostname = self.hostname
        favorite = self.favorite
        setup_finished = self.setup_finished

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sbc is not UNSET:
            field_dict["sbc"] = sbc
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if setup_finished is not UNSET:
            field_dict["setup_finished"] = setup_finished

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        sbc: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.sbc, Unset):
            sbc = (None, str(self.sbc.value).encode(), "text/plain")

        hostname = (
            self.hostname if isinstance(self.hostname, Unset) else (None, str(self.hostname).encode(), "text/plain")
        )
        favorite = (
            self.favorite if isinstance(self.favorite, Unset) else (None, str(self.favorite).encode(), "text/plain")
        )
        setup_finished = (
            self.setup_finished
            if isinstance(self.setup_finished, Unset)
            else (None, str(self.setup_finished).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if sbc is not UNSET:
            field_dict["sbc"] = sbc
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if setup_finished is not UNSET:
            field_dict["setup_finished"] = setup_finished

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _sbc = d.pop("sbc", UNSET)
        sbc: Union[Unset, SbcEnum]
        if isinstance(_sbc, Unset):
            sbc = UNSET
        else:
            sbc = SbcEnum(_sbc)

        hostname = d.pop("hostname", UNSET)

        favorite = d.pop("favorite", UNSET)

        setup_finished = d.pop("setup_finished", UNSET)

        pi_request = cls(
            sbc=sbc,
            hostname=hostname,
            favorite=favorite,
            setup_finished=setup_finished,
        )

        pi_request.additional_properties = d
        return pi_request

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
