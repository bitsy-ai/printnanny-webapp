import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="GcodeFile")


@attr.s(auto_attribs=True)
class GcodeFile:
    """
    Attributes:
        id (int):
        name (str):
        file (str):
        hash_ (str):
        created_dt (datetime.datetime):
        user (int):
    """

    id: int
    name: str
    file: str
    hash_: str
    created_dt: datetime.datetime
    user: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        file = self.file
        hash_ = self.hash_
        created_dt = self.created_dt.isoformat()

        user = self.user

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "file": file,
                "hash": hash_,
                "created_dt": created_dt,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        file = d.pop("file")

        hash_ = d.pop("hash")

        created_dt = isoparse(d.pop("created_dt"))

        user = d.pop("user")

        gcode_file = cls(
            id=id,
            name=name,
            file=file,
            hash_=hash_,
            created_dt=created_dt,
            user=user,
        )

        gcode_file.additional_properties = d
        return gcode_file

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
