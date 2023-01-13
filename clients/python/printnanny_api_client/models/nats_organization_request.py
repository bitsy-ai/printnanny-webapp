from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nats_organization_request_json import NatsOrganizationRequestJson


T = TypeVar("T", bound="NatsOrganizationRequest")


@attr.s(auto_attribs=True)
class NatsOrganizationRequest:
    """
    Attributes:
        name (str): The name of the organization
        slug (str): The name in all lowercase, suitable for URL identification
        imports (List[int]):
        exports (List[int]):
        is_active (Union[Unset, bool]):
        json (Union[Unset, NatsOrganizationRequestJson]): Output of `nsc describe account`
        jetstream_enabled (Union[Unset, bool]): Enable JetStream for all users/apps belonging to NatsOrganization
            account
        jetstream_max_mem (Union[Unset, str]): JetStream memory resource limits (shared across all users/apps beloning
            to NatsOrganization account)
        jetstream_max_file (Union[Unset, str]): JetStream file resource limits (shared across all users/apps beloning to
            NatsOrganization account)
        jetstream_max_streams (Union[Unset, int]): JetStream max number of streams (shared across all users/apps
            beloning to NatsOrganization account)
        jetstream_max_consumers (Union[Unset, int]): JetStream max number of consumers (shared across all users/apps
            beloning to NatsOrganization account)
    """

    name: str
    slug: str
    imports: List[int]
    exports: List[int]
    is_active: Union[Unset, bool] = UNSET
    json: Union[Unset, "NatsOrganizationRequestJson"] = UNSET
    jetstream_enabled: Union[Unset, bool] = UNSET
    jetstream_max_mem: Union[Unset, str] = UNSET
    jetstream_max_file: Union[Unset, str] = UNSET
    jetstream_max_streams: Union[Unset, int] = UNSET
    jetstream_max_consumers: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        slug = self.slug
        imports = self.imports

        exports = self.exports

        is_active = self.is_active
        json: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.json, Unset):
            json = self.json.to_dict()

        jetstream_enabled = self.jetstream_enabled
        jetstream_max_mem = self.jetstream_max_mem
        jetstream_max_file = self.jetstream_max_file
        jetstream_max_streams = self.jetstream_max_streams
        jetstream_max_consumers = self.jetstream_max_consumers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "slug": slug,
                "imports": imports,
                "exports": exports,
            }
        )
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if json is not UNSET:
            field_dict["json"] = json
        if jetstream_enabled is not UNSET:
            field_dict["jetstream_enabled"] = jetstream_enabled
        if jetstream_max_mem is not UNSET:
            field_dict["jetstream_max_mem"] = jetstream_max_mem
        if jetstream_max_file is not UNSET:
            field_dict["jetstream_max_file"] = jetstream_max_file
        if jetstream_max_streams is not UNSET:
            field_dict["jetstream_max_streams"] = jetstream_max_streams
        if jetstream_max_consumers is not UNSET:
            field_dict["jetstream_max_consumers"] = jetstream_max_consumers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nats_organization_request_json import NatsOrganizationRequestJson

        d = src_dict.copy()
        name = d.pop("name")

        slug = d.pop("slug")

        imports = cast(List[int], d.pop("imports"))

        exports = cast(List[int], d.pop("exports"))

        is_active = d.pop("is_active", UNSET)

        _json = d.pop("json", UNSET)
        json: Union[Unset, NatsOrganizationRequestJson]
        if isinstance(_json, Unset):
            json = UNSET
        else:
            json = NatsOrganizationRequestJson.from_dict(_json)

        jetstream_enabled = d.pop("jetstream_enabled", UNSET)

        jetstream_max_mem = d.pop("jetstream_max_mem", UNSET)

        jetstream_max_file = d.pop("jetstream_max_file", UNSET)

        jetstream_max_streams = d.pop("jetstream_max_streams", UNSET)

        jetstream_max_consumers = d.pop("jetstream_max_consumers", UNSET)

        nats_organization_request = cls(
            name=name,
            slug=slug,
            imports=imports,
            exports=exports,
            is_active=is_active,
            json=json,
            jetstream_enabled=jetstream_enabled,
            jetstream_max_mem=jetstream_max_mem,
            jetstream_max_file=jetstream_max_file,
            jetstream_max_streams=jetstream_max_streams,
            jetstream_max_consumers=jetstream_max_consumers,
        )

        nats_organization_request.additional_properties = d
        return nats_organization_request

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
