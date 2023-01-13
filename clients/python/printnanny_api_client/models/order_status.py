import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.order_status_type import OrderStatusType

T = TypeVar("T", bound="OrderStatus")


@attr.s(auto_attribs=True)
class OrderStatus:
    """
    Attributes:
        id (int):
        deleted (datetime.datetime):
        created_dt (datetime.datetime):
        status (OrderStatusType):
        order (str):
    """

    id: int
    deleted: datetime.datetime
    created_dt: datetime.datetime
    status: OrderStatusType
    order: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        deleted = self.deleted.isoformat()

        created_dt = self.created_dt.isoformat()

        status = self.status.value

        order = self.order

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "deleted": deleted,
                "created_dt": created_dt,
                "status": status,
                "order": order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        deleted = isoparse(d.pop("deleted"))

        created_dt = isoparse(d.pop("created_dt"))

        status = OrderStatusType(d.pop("status"))

        order = d.pop("order")

        order_status = cls(
            id=id,
            deleted=deleted,
            created_dt=created_dt,
            status=status,
            order=order,
        )

        order_status.additional_properties = d
        return order_status

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
