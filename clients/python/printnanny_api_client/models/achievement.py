import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.achievement_type_enum import AchievementTypeEnum

T = TypeVar("T", bound="Achievement")


@attr.s(auto_attribs=True)
class Achievement:
    """
    Attributes:
        created_dt (datetime.datetime):
        type (AchievementTypeEnum):
        label (str):
        user (int):
    """

    created_dt: datetime.datetime
    type: AchievementTypeEnum
    label: str
    user: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_dt = self.created_dt.isoformat()

        type = self.type.value

        label = self.label
        user = self.user

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_dt": created_dt,
                "type": type,
                "label": label,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_dt = isoparse(d.pop("created_dt"))

        type = AchievementTypeEnum(d.pop("type"))

        label = d.pop("label")

        user = d.pop("user")

        achievement = cls(
            created_dt=created_dt,
            type=type,
            label=label,
            user=user,
        )

        achievement.additional_properties = d
        return achievement

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
