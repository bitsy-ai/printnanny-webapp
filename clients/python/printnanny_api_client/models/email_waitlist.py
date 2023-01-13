import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="EmailWaitlist")


@attr.s(auto_attribs=True)
class EmailWaitlist:
    """
    Attributes:
        id (int):
        created_dt (datetime.datetime):
        email (str):
    """

    id: int
    created_dt: datetime.datetime
    email: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        created_dt = self.created_dt.isoformat()

        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_dt": created_dt,
                "email": email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        created_dt = isoparse(d.pop("created_dt"))

        email = d.pop("email")

        email_waitlist = cls(
            id=id,
            created_dt=created_dt,
            email=email,
        )

        email_waitlist.additional_properties = d
        return email_waitlist

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
