from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.octo_print_print_job_payload_request_position import OctoPrintPrintJobPayloadRequestPosition


T = TypeVar("T", bound="OctoPrintPrintJobPayloadRequest")


@attr.s(auto_attribs=True)
class OctoPrintPrintJobPayloadRequest:
    """Serialize OctoPrint print job status events:
    https://docs.octoprint.org/en/master/events/index.html?highlight=events#printing

        Attributes:
            name (str):
            path (str):
            origin (str):
            position (OctoPrintPrintJobPayloadRequestPosition):
            size (Union[Unset, int]):
            time (Union[Unset, float]):
    """

    name: str
    path: str
    origin: str
    position: "OctoPrintPrintJobPayloadRequestPosition"
    size: Union[Unset, int] = UNSET
    time: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        path = self.path
        origin = self.origin
        position = self.position.to_dict()

        size = self.size
        time = self.time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "path": path,
                "origin": origin,
                "position": position,
            }
        )
        if size is not UNSET:
            field_dict["size"] = size
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.octo_print_print_job_payload_request_position import OctoPrintPrintJobPayloadRequestPosition

        d = src_dict.copy()
        name = d.pop("name")

        path = d.pop("path")

        origin = d.pop("origin")

        position = OctoPrintPrintJobPayloadRequestPosition.from_dict(d.pop("position"))

        size = d.pop("size", UNSET)

        time = d.pop("time", UNSET)

        octo_print_print_job_payload_request = cls(
            name=name,
            path=path,
            origin=origin,
            position=position,
            size=size,
            time=time,
        )

        octo_print_print_job_payload_request.additional_properties = d
        return octo_print_print_job_payload_request

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
