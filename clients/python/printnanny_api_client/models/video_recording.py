import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="VideoRecording")


@attr.s(auto_attribs=True)
class VideoRecording:
    """
    Attributes:
        id (int):
        mjr_upload_url (str):
        start_dt (datetime.datetime):
        name (str):
        user (int):
        end_dt (Union[Unset, None, datetime.datetime]):
        mjr_recording (Union[Unset, None, str]):
    """

    id: int
    mjr_upload_url: str
    start_dt: datetime.datetime
    name: str
    user: int
    end_dt: Union[Unset, None, datetime.datetime] = UNSET
    mjr_recording: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        mjr_upload_url = self.mjr_upload_url
        start_dt = self.start_dt.isoformat()

        name = self.name
        user = self.user
        end_dt: Union[Unset, None, str] = UNSET
        if not isinstance(self.end_dt, Unset):
            end_dt = self.end_dt.isoformat() if self.end_dt else None

        mjr_recording = self.mjr_recording

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "mjr_upload_url": mjr_upload_url,
                "start_dt": start_dt,
                "name": name,
                "user": user,
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
        id = d.pop("id")

        mjr_upload_url = d.pop("mjr_upload_url")

        start_dt = isoparse(d.pop("start_dt"))

        name = d.pop("name")

        user = d.pop("user")

        _end_dt = d.pop("end_dt", UNSET)
        end_dt: Union[Unset, None, datetime.datetime]
        if _end_dt is None:
            end_dt = None
        elif isinstance(_end_dt, Unset):
            end_dt = UNSET
        else:
            end_dt = isoparse(_end_dt)

        mjr_recording = d.pop("mjr_recording", UNSET)

        video_recording = cls(
            id=id,
            mjr_upload_url=mjr_upload_url,
            start_dt=start_dt,
            name=name,
            user=user,
            end_dt=end_dt,
            mjr_recording=mjr_recording,
        )

        video_recording.additional_properties = d
        return video_recording

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
