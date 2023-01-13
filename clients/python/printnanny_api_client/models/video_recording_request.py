import datetime
from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="VideoRecordingRequest")


@attr.s(auto_attribs=True)
class VideoRecordingRequest:
    """
    Attributes:
        start_dt (datetime.datetime):
        name (str):
        end_dt (Union[Unset, None, datetime.datetime]):
        mjr_recording (Union[Unset, None, File]):
    """

    start_dt: datetime.datetime
    name: str
    end_dt: Union[Unset, None, datetime.datetime] = UNSET
    mjr_recording: Union[Unset, None, File] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_dt = self.start_dt.isoformat()

        name = self.name
        end_dt: Union[Unset, None, str] = UNSET
        if not isinstance(self.end_dt, Unset):
            end_dt = self.end_dt.isoformat() if self.end_dt else None

        mjr_recording: Union[Unset, None, FileJsonType] = UNSET
        if not isinstance(self.mjr_recording, Unset):
            mjr_recording = self.mjr_recording.to_tuple() if self.mjr_recording else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_dt": start_dt,
                "name": name,
            }
        )
        if end_dt is not UNSET:
            field_dict["end_dt"] = end_dt
        if mjr_recording is not UNSET:
            field_dict["mjr_recording"] = mjr_recording

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        start_dt = self.start_dt.isoformat().encode()

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        end_dt: Union[Unset, None, bytes] = UNSET
        if not isinstance(self.end_dt, Unset):
            end_dt = self.end_dt.isoformat().encode() if self.end_dt else None

        mjr_recording: Union[Unset, None, FileJsonType] = UNSET
        if not isinstance(self.mjr_recording, Unset):
            mjr_recording = self.mjr_recording.to_tuple() if self.mjr_recording else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "start_dt": start_dt,
                "name": name,
            }
        )
        if end_dt is not UNSET:
            field_dict["end_dt"] = end_dt
        if mjr_recording is not UNSET:
            field_dict["mjr_recording"] = mjr_recording

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start_dt = isoparse(d.pop("start_dt"))

        name = d.pop("name")

        _end_dt = d.pop("end_dt", UNSET)
        end_dt: Union[Unset, None, datetime.datetime]
        if _end_dt is None:
            end_dt = None
        elif isinstance(_end_dt, Unset):
            end_dt = UNSET
        else:
            end_dt = isoparse(_end_dt)

        _mjr_recording = d.pop("mjr_recording", UNSET)
        mjr_recording: Union[Unset, None, File]
        if _mjr_recording is None:
            mjr_recording = None
        elif isinstance(_mjr_recording, Unset):
            mjr_recording = UNSET
        else:
            mjr_recording = File(payload=BytesIO(_mjr_recording))

        video_recording_request = cls(
            start_dt=start_dt,
            name=name,
            end_dt=end_dt,
            mjr_recording=mjr_recording,
        )

        video_recording_request.additional_properties = d
        return video_recording_request

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
