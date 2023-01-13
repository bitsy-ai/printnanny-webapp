from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.octo_print_printer_status_subject_pattern_enum import OctoPrintPrinterStatusSubjectPatternEnum
from ..models.octo_print_printer_status_type import OctoPrintPrinterStatusType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.octo_print_printer_status_request_payload import OctoPrintPrinterStatusRequestPayload


T = TypeVar("T", bound="OctoPrintPrinterStatusRequest")


@attr.s(auto_attribs=True)
class OctoPrintPrinterStatusRequest:
    """
    Attributes:
        subject_pattern (OctoPrintPrinterStatusSubjectPatternEnum):
        event_type (OctoPrintPrinterStatusType):
        octoprint_server (int):
        pi (int):
        payload (Union[Unset, None, OctoPrintPrinterStatusRequestPayload]):
    """

    subject_pattern: OctoPrintPrinterStatusSubjectPatternEnum
    event_type: OctoPrintPrinterStatusType
    octoprint_server: int
    pi: int
    payload: Union[Unset, None, "OctoPrintPrinterStatusRequestPayload"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subject_pattern = self.subject_pattern.value

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
                "subject_pattern": subject_pattern,
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
        from ..models.octo_print_printer_status_request_payload import OctoPrintPrinterStatusRequestPayload

        d = src_dict.copy()
        subject_pattern = OctoPrintPrinterStatusSubjectPatternEnum(d.pop("subject_pattern"))

        event_type = OctoPrintPrinterStatusType(d.pop("event_type"))

        octoprint_server = d.pop("octoprint_server")

        pi = d.pop("pi")

        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, None, OctoPrintPrinterStatusRequestPayload]
        if _payload is None:
            payload = None
        elif isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = OctoPrintPrinterStatusRequestPayload.from_dict(_payload)

        octo_print_printer_status_request = cls(
            subject_pattern=subject_pattern,
            event_type=event_type,
            octoprint_server=octoprint_server,
            pi=pi,
            payload=payload,
        )

        octo_print_printer_status_request.additional_properties = d
        return octo_print_printer_status_request

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
