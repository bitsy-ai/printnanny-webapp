from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.octo_print_print_job_status_subject_pattern_enum import OctoPrintPrintJobStatusSubjectPatternEnum
from ..models.octo_print_print_job_status_type import OctoPrintPrintJobStatusType

if TYPE_CHECKING:
    from ..models.octo_print_print_job_payload_request import OctoPrintPrintJobPayloadRequest


T = TypeVar("T", bound="OctoPrintPrintJobStatusRequest")


@attr.s(auto_attribs=True)
class OctoPrintPrintJobStatusRequest:
    """
    Attributes:
        subject_pattern (OctoPrintPrintJobStatusSubjectPatternEnum):
        payload (OctoPrintPrintJobPayloadRequest): Serialize OctoPrint print job status events:
            https://docs.octoprint.org/en/master/events/index.html?highlight=events#printing
        event_type (OctoPrintPrintJobStatusType):
        octoprint_server (int):
        pi (int):
    """

    subject_pattern: OctoPrintPrintJobStatusSubjectPatternEnum
    payload: "OctoPrintPrintJobPayloadRequest"
    event_type: OctoPrintPrintJobStatusType
    octoprint_server: int
    pi: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subject_pattern = self.subject_pattern.value

        payload = self.payload.to_dict()

        event_type = self.event_type.value

        octoprint_server = self.octoprint_server
        pi = self.pi

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subject_pattern": subject_pattern,
                "payload": payload,
                "event_type": event_type,
                "octoprint_server": octoprint_server,
                "pi": pi,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.octo_print_print_job_payload_request import OctoPrintPrintJobPayloadRequest

        d = src_dict.copy()
        subject_pattern = OctoPrintPrintJobStatusSubjectPatternEnum(d.pop("subject_pattern"))

        payload = OctoPrintPrintJobPayloadRequest.from_dict(d.pop("payload"))

        event_type = OctoPrintPrintJobStatusType(d.pop("event_type"))

        octoprint_server = d.pop("octoprint_server")

        pi = d.pop("pi")

        octo_print_print_job_status_request = cls(
            subject_pattern=subject_pattern,
            payload=payload,
            event_type=event_type,
            octoprint_server=octoprint_server,
            pi=pi,
        )

        octo_print_print_job_status_request.additional_properties = d
        return octo_print_print_job_status_request

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
