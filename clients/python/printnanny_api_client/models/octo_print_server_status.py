import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.octo_print_server_status_subject_pattern_enum import OctoPrintServerStatusSubjectPatternEnum
from ..models.octo_print_server_status_type import OctoPrintServerStatusType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.octo_print_server_status_payload import OctoPrintServerStatusPayload


T = TypeVar("T", bound="OctoPrintServerStatus")


@attr.s(auto_attribs=True)
class OctoPrintServerStatus:
    """
    Attributes:
        id (str):
        subject_pattern (OctoPrintServerStatusSubjectPatternEnum):
        created_dt (datetime.datetime):
        event_type (OctoPrintServerStatusType):
        octoprint_server (int):
        pi (int):
        payload (Union[Unset, None, OctoPrintServerStatusPayload]):
    """

    id: str
    subject_pattern: OctoPrintServerStatusSubjectPatternEnum
    created_dt: datetime.datetime
    event_type: OctoPrintServerStatusType
    octoprint_server: int
    pi: int
    payload: Union[Unset, None, "OctoPrintServerStatusPayload"] = UNSET
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
        from ..models.octo_print_server_status_payload import OctoPrintServerStatusPayload

        d = src_dict.copy()
        id = d.pop("id")

        subject_pattern = OctoPrintServerStatusSubjectPatternEnum(d.pop("subject_pattern"))

        created_dt = isoparse(d.pop("created_dt"))

        event_type = OctoPrintServerStatusType(d.pop("event_type"))

        octoprint_server = d.pop("octoprint_server")

        pi = d.pop("pi")

        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, None, OctoPrintServerStatusPayload]
        if _payload is None:
            payload = None
        elif isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = OctoPrintServerStatusPayload.from_dict(_payload)

        octo_print_server_status = cls(
            id=id,
            subject_pattern=subject_pattern,
            created_dt=created_dt,
            event_type=event_type,
            octoprint_server=octoprint_server,
            pi=pi,
            payload=payload,
        )

        octo_print_server_status.additional_properties = d
        return octo_print_server_status

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
