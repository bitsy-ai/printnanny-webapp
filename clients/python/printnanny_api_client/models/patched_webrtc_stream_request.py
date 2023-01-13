from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.janus_config_type import JanusConfigType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedWebrtcStreamRequest")


@attr.s(auto_attribs=True)
class PatchedWebrtcStreamRequest:
    """
    Attributes:
        active (Union[Unset, bool]):
        config_type (Union[Unset, JanusConfigType]):
    """

    active: Union[Unset, bool] = UNSET
    config_type: Union[Unset, JanusConfigType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active = self.active
        config_type: Union[Unset, str] = UNSET
        if not isinstance(self.config_type, Unset):
            config_type = self.config_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if config_type is not UNSET:
            field_dict["config_type"] = config_type

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        active = self.active if isinstance(self.active, Unset) else (None, str(self.active).encode(), "text/plain")
        config_type: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.config_type, Unset):
            config_type = (None, str(self.config_type.value).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if config_type is not UNSET:
            field_dict["config_type"] = config_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        active = d.pop("active", UNSET)

        _config_type = d.pop("config_type", UNSET)
        config_type: Union[Unset, JanusConfigType]
        if isinstance(_config_type, Unset):
            config_type = UNSET
        else:
            config_type = JanusConfigType(_config_type)

        patched_webrtc_stream_request = cls(
            active=active,
            config_type=config_type,
        )

        patched_webrtc_stream_request.additional_properties = d
        return patched_webrtc_stream_request

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
