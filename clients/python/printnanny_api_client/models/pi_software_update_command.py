import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.pi_software_update_command_subject_pattern_enum import PiSoftwareUpdateCommandSubjectPatternEnum
from ..models.pi_software_update_command_type import PiSoftwareUpdateCommandType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pi_software_update_payload import PiSoftwareUpdatePayload


T = TypeVar("T", bound="PiSoftwareUpdateCommand")


@attr.s(auto_attribs=True)
class PiSoftwareUpdateCommand:
    """
    Attributes:
        payload (PiSoftwareUpdatePayload):
        subject_pattern (PiSoftwareUpdateCommandSubjectPatternEnum):
        version (str):
        event_type (PiSoftwareUpdateCommandType):
        pi (int):
        id (Union[Unset, str]):
        created_dt (Union[Unset, datetime.datetime]):
    """

    payload: "PiSoftwareUpdatePayload"
    subject_pattern: PiSoftwareUpdateCommandSubjectPatternEnum
    version: str
    event_type: PiSoftwareUpdateCommandType
    pi: int
    id: Union[Unset, str] = UNSET
    created_dt: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payload = self.payload.to_dict()

        subject_pattern = self.subject_pattern.value

        version = self.version
        event_type = self.event_type.value

        pi = self.pi
        id = self.id
        created_dt: Union[Unset, str] = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payload": payload,
                "subject_pattern": subject_pattern,
                "version": version,
                "event_type": event_type,
                "pi": pi,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if created_dt is not UNSET:
            field_dict["created_dt"] = created_dt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pi_software_update_payload import PiSoftwareUpdatePayload

        d = src_dict.copy()
        payload = PiSoftwareUpdatePayload.from_dict(d.pop("payload"))

        subject_pattern = PiSoftwareUpdateCommandSubjectPatternEnum(d.pop("subject_pattern"))

        version = d.pop("version")

        event_type = PiSoftwareUpdateCommandType(d.pop("event_type"))

        pi = d.pop("pi")

        id = d.pop("id", UNSET)

        _created_dt = d.pop("created_dt", UNSET)
        created_dt: Union[Unset, datetime.datetime]
        if isinstance(_created_dt, Unset):
            created_dt = UNSET
        else:
            created_dt = isoparse(_created_dt)

        pi_software_update_command = cls(
            payload=payload,
            subject_pattern=subject_pattern,
            version=version,
            event_type=event_type,
            pi=pi,
            id=id,
            created_dt=created_dt,
        )

        pi_software_update_command.additional_properties = d
        return pi_software_update_command

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
