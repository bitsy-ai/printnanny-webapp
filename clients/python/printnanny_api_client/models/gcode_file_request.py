from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar

import attr

from ..types import File, Unset

T = TypeVar("T", bound="GcodeFileRequest")


@attr.s(auto_attribs=True)
class GcodeFileRequest:
    """
    Attributes:
        name (str):
        file (File):
        hash_ (str):
    """

    name: str
    file: File
    hash_: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        file = self.file.to_tuple()

        hash_ = self.hash_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "file": file,
                "hash": hash_,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        file = self.file.to_tuple()

        hash_ = self.hash_ if isinstance(self.hash_, Unset) else (None, str(self.hash_).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "name": name,
                "file": file,
                "hash": hash_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        file = File(payload=BytesIO(d.pop("file")))

        hash_ = d.pop("hash")

        gcode_file_request = cls(
            name=name,
            file=file,
            hash_=hash_,
        )

        gcode_file_request.additional_properties = d
        return gcode_file_request

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
