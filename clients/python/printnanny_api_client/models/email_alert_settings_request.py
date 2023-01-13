import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.event_types_enum import EventTypesEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="EmailAlertSettingsRequest")


@attr.s(auto_attribs=True)
class EmailAlertSettingsRequest:
    """
    Attributes:
        progress_percent (Union[Unset, int]):
        enabled (Union[Unset, bool]):
        event_types (Union[Unset, List[EventTypesEnum]]):
    """

    progress_percent: Union[Unset, int] = UNSET
    enabled: Union[Unset, bool] = UNSET
    event_types: Union[Unset, List[EventTypesEnum]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        progress_percent = self.progress_percent
        enabled = self.enabled
        event_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.event_types, Unset):
            event_types = []
            for event_types_item_data in self.event_types:
                event_types_item = event_types_item_data.value

                event_types.append(event_types_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if progress_percent is not UNSET:
            field_dict["progress_percent"] = progress_percent
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if event_types is not UNSET:
            field_dict["event_types"] = event_types

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        progress_percent = (
            self.progress_percent
            if isinstance(self.progress_percent, Unset)
            else (None, str(self.progress_percent).encode(), "text/plain")
        )
        enabled = self.enabled if isinstance(self.enabled, Unset) else (None, str(self.enabled).encode(), "text/plain")
        event_types: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.event_types, Unset):
            _temp_event_types = []
            for event_types_item_data in self.event_types:
                event_types_item = event_types_item_data.value

                _temp_event_types.append(event_types_item)
            event_types = (None, json.dumps(_temp_event_types).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if progress_percent is not UNSET:
            field_dict["progress_percent"] = progress_percent
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if event_types is not UNSET:
            field_dict["event_types"] = event_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        progress_percent = d.pop("progress_percent", UNSET)

        enabled = d.pop("enabled", UNSET)

        event_types = []
        _event_types = d.pop("event_types", UNSET)
        for event_types_item_data in _event_types or []:
            event_types_item = EventTypesEnum(event_types_item_data)

            event_types.append(event_types_item)

        email_alert_settings_request = cls(
            progress_percent=progress_percent,
            enabled=enabled,
            event_types=event_types,
        )

        email_alert_settings_request.additional_properties = d
        return email_alert_settings_request

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
