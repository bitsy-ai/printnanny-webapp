import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.gcode_event_type import GcodeEventType
from ..models.octo_print_gcode_event_subject_pattern_enum import OctoPrintGcodeEventSubjectPatternEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.octo_print_gcode_event_payload import OctoPrintGcodeEventPayload


T = TypeVar("T", bound="OctoPrintGcodeEvent")


@attr.s(auto_attribs=True)
class OctoPrintGcodeEvent:
    """
    Attributes:
        id (str):
        subject_pattern (OctoPrintGcodeEventSubjectPatternEnum):
        created_dt (datetime.datetime):
        event_type (GcodeEventType):
        octoprint_server (int):
        pi (int):
        payload (Union[Unset, None, OctoPrintGcodeEventPayload]):
    """

    id: str
    subject_pattern: OctoPrintGcodeEventSubjectPatternEnum
    created_dt: datetime.datetime
    event_type: GcodeEventType
    octoprint_server: int
    pi: int
    payload: Union[Unset, None, "OctoPrintGcodeEventPayload"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        subject_pattern = self.subject_pattern.value

        created_dt = self.created_dt.isoformat()

        event_type = self.event_type.value

        octoprint_server = self.octoprint_server
        pi = self.pi
        payload: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict() if self.payload else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "subject_pattern": subject_pattern,
                "created_dt": created_dt,
                "event_type": event_type,
                "octoprint_server": octoprint_server,
                "pi": pi,
            }
        )
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.octo_print_gcode_event_payload import OctoPrintGcodeEventPayload

        d = src_dict.copy()
        id = d.pop("id")

        subject_pattern = OctoPrintGcodeEventSubjectPatternEnum(d.pop("subject_pattern"))

        created_dt = isoparse(d.pop("created_dt"))

        event_type = GcodeEventType(d.pop("event_type"))

        octoprint_server = d.pop("octoprint_server")

        pi = d.pop("pi")

        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, None, OctoPrintGcodeEventPayload]
        if _payload is None:
            payload = None
        elif isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = OctoPrintGcodeEventPayload.from_dict(_payload)

        octo_print_gcode_event = cls(
            id=id,
            subject_pattern=subject_pattern,
            created_dt=created_dt,
            event_type=event_type,
            octoprint_server=octoprint_server,
            pi=pi,
            payload=payload,
        )

        octo_print_gcode_event.additional_properties = d
        return octo_print_gcode_event

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
