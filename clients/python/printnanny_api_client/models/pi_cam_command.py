import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.pi_cam_command_subject_pattern_enum import PiCamCommandSubjectPatternEnum
from ..models.pi_cam_command_type import PiCamCommandType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pi_cam_command_payload import PiCamCommandPayload


T = TypeVar("T", bound="PiCamCommand")


@attr.s(auto_attribs=True)
class PiCamCommand:
    """
    Attributes:
        subject_pattern (PiCamCommandSubjectPatternEnum):
        event_type (PiCamCommandType):
        pi (int):
        id (Union[Unset, str]):
        created_dt (Union[Unset, datetime.datetime]):
        payload (Union[Unset, None, PiCamCommandPayload]):
    """

    subject_pattern: PiCamCommandSubjectPatternEnum
    event_type: PiCamCommandType
    pi: int
    id: Union[Unset, str] = UNSET
    created_dt: Union[Unset, datetime.datetime] = UNSET
    payload: Union[Unset, None, "PiCamCommandPayload"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subject_pattern = self.subject_pattern.value

        event_type = self.event_type.value

        pi = self.pi
        id = self.id
        created_dt: Union[Unset, str] = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        payload: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict() if self.payload else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subject_pattern": subject_pattern,
                "event_type": event_type,
                "pi": pi,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if created_dt is not UNSET:
            field_dict["created_dt"] = created_dt
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pi_cam_command_payload import PiCamCommandPayload

        d = src_dict.copy()
        subject_pattern = PiCamCommandSubjectPatternEnum(d.pop("subject_pattern"))

        event_type = PiCamCommandType(d.pop("event_type"))

        pi = d.pop("pi")

        id = d.pop("id", UNSET)

        _created_dt = d.pop("created_dt", UNSET)
        created_dt: Union[Unset, datetime.datetime]
        if isinstance(_created_dt, Unset):
            created_dt = UNSET
        else:
            created_dt = isoparse(_created_dt)

        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, None, PiCamCommandPayload]
        if _payload is None:
            payload = None
        elif isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = PiCamCommandPayload.from_dict(_payload)

        pi_cam_command = cls(
            subject_pattern=subject_pattern,
            event_type=event_type,
            pi=pi,
            id=id,
            created_dt=created_dt,
            payload=payload,
        )

        pi_cam_command.additional_properties = d
        return pi_cam_command

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
