from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nats_organization_user_json import NatsOrganizationUserJson


T = TypeVar("T", bound="NatsOrganizationUser")


@attr.s(auto_attribs=True)
class NatsOrganizationUser:
    """
    Attributes:
        id (int):
        organization (int):
        creds (str):
        app_name (Union[Unset, str]):
        json (Union[Unset, NatsOrganizationUserJson]): Output of `nsc describe account`
    """

    id: int
    organization: int
    creds: str
    app_name: Union[Unset, str] = UNSET
    json: Union[Unset, "NatsOrganizationUserJson"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        organization = self.organization
        creds = self.creds
        app_name = self.app_name
        json: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.json, Unset):
            json = self.json.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "organization": organization,
                "creds": creds,
            }
        )
        if app_name is not UNSET:
            field_dict["app_name"] = app_name
        if json is not UNSET:
            field_dict["json"] = json

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nats_organization_user_json import NatsOrganizationUserJson

        d = src_dict.copy()
        id = d.pop("id")

        organization = d.pop("organization")

        creds = d.pop("creds")

        app_name = d.pop("app_name", UNSET)

        _json = d.pop("json", UNSET)
        json: Union[Unset, NatsOrganizationUserJson]
        if isinstance(_json, Unset):
            json = UNSET
        else:
            json = NatsOrganizationUserJson.from_dict(_json)

        nats_organization_user = cls(
            id=id,
            organization=organization,
            creds=creds,
            app_name=app_name,
            json=json,
        )

        nats_organization_user.additional_properties = d
        return nats_organization_user

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
