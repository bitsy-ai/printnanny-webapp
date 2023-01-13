import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="OctoPrintBackup")


@attr.s(auto_attribs=True)
class OctoPrintBackup:
    """
    Attributes:
        id (int):
        deleted (datetime.datetime):
        created_dt (datetime.datetime):
        hostname (str):
        name (str):
        octoprint_version (str):
        file (str):
        user (int):
    """

    id: int
    deleted: datetime.datetime
    created_dt: datetime.datetime
    hostname: str
    name: str
    octoprint_version: str
    file: str
    user: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        deleted = self.deleted.isoformat()

        created_dt = self.created_dt.isoformat()

        hostname = self.hostname
        name = self.name
        octoprint_version = self.octoprint_version
        file = self.file
        user = self.user

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "deleted": deleted,
                "created_dt": created_dt,
                "hostname": hostname,
                "name": name,
                "octoprint_version": octoprint_version,
                "file": file,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        deleted = isoparse(d.pop("deleted"))

        created_dt = isoparse(d.pop("created_dt"))

        hostname = d.pop("hostname")

        name = d.pop("name")

        octoprint_version = d.pop("octoprint_version")

        file = d.pop("file")

        user = d.pop("user")

        octo_print_backup = cls(
            id=id,
            deleted=deleted,
            created_dt=created_dt,
            hostname=hostname,
            name=name,
            octoprint_version=octoprint_version,
            file=file,
            user=user,
        )

        octo_print_backup.additional_properties = d
        return octo_print_backup

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
