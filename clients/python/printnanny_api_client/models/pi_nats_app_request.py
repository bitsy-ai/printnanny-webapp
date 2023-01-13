from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nats_organization_request import NatsOrganizationRequest
    from ..models.pi_nats_app_request_json import PiNatsAppRequestJson


T = TypeVar("T", bound="PiNatsAppRequest")


@attr.s(auto_attribs=True)
class PiNatsAppRequest:
    """
    Attributes:
        pi (int):
        organization (NatsOrganizationRequest):
        organization_user (int):
        app_name (Union[Unset, str]):
        json (Union[Unset, PiNatsAppRequestJson]): Output of `nsc describe account`
    """

    pi: int
    organization: "NatsOrganizationRequest"
    organization_user: int
    app_name: Union[Unset, str] = UNSET
    json: Union[Unset, "PiNatsAppRequestJson"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pi = self.pi
        organization = self.organization.to_dict()

        organization_user = self.organization_user
        app_name = self.app_name
        json: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.json, Unset):
            json = self.json.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pi": pi,
                "organization": organization,
                "organization_user": organization_user,
            }
        )
        if app_name is not UNSET:
            field_dict["app_name"] = app_name
        if json is not UNSET:
            field_dict["json"] = json

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nats_organization_request import NatsOrganizationRequest
        from ..models.pi_nats_app_request_json import PiNatsAppRequestJson

        d = src_dict.copy()
        pi = d.pop("pi")

        organization = NatsOrganizationRequest.from_dict(d.pop("organization"))

        organization_user = d.pop("organization_user")

        app_name = d.pop("app_name", UNSET)

        _json = d.pop("json", UNSET)
        json: Union[Unset, PiNatsAppRequestJson]
        if isinstance(_json, Unset):
            json = UNSET
        else:
            json = PiNatsAppRequestJson.from_dict(_json)

        pi_nats_app_request = cls(
            pi=pi,
            organization=organization,
            organization_user=organization_user,
            app_name=app_name,
            json=json,
        )

        pi_nats_app_request.additional_properties = d
        return pi_nats_app_request

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
