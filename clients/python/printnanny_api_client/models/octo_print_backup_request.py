from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar

import attr

from ..types import File, Unset

T = TypeVar("T", bound="OctoPrintBackupRequest")


@attr.s(auto_attribs=True)
class OctoPrintBackupRequest:
    """
    Attributes:
        hostname (str):
        name (str):
        octoprint_version (str):
        file (File):
    """

    hostname: str
    name: str
    octoprint_version: str
    file: File
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hostname = self.hostname
        name = self.name
        octoprint_version = self.octoprint_version
        file = self.file.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hostname": hostname,
                "name": name,
                "octoprint_version": octoprint_version,
                "file": file,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        hostname = (
            self.hostname if isinstance(self.hostname, Unset) else (None, str(self.hostname).encode(), "text/plain")
        )
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        octoprint_version = (
            self.octoprint_version
            if isinstance(self.octoprint_version, Unset)
            else (None, str(self.octoprint_version).encode(), "text/plain")
        )
        file = self.file.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "hostname": hostname,
                "name": name,
                "octoprint_version": octoprint_version,
                "file": file,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hostname = d.pop("hostname")

        name = d.pop("name")

        octoprint_version = d.pop("octoprint_version")

        file = File(payload=BytesIO(d.pop("file")))

        octo_print_backup_request = cls(
            hostname=hostname,
            name=name,
            octoprint_version=octoprint_version,
            file=file,
        )

        octo_print_backup_request.additional_properties = d
        return octo_print_backup_request

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
