import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nats_organization_json import NatsOrganizationJson


T = TypeVar("T", bound="NatsOrganization")


@attr.s(auto_attribs=True)
class NatsOrganization:
    """
    Attributes:
        id (int):
        name (str): The name of the organization
        created (datetime.datetime):
        modified (datetime.datetime):
        slug (str): The name in all lowercase, suitable for URL identification
        imports (List[int]):
        exports (List[int]):
        users (List[int]):
        is_active (Union[Unset, bool]):
        json (Union[Unset, NatsOrganizationJson]): Output of `nsc describe account`
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

    id: int
    name: str
    created: datetime.datetime
    modified: datetime.datetime
    slug: str
    imports: List[int]
    exports: List[int]
    users: List[int]
    is_active: Union[Unset, bool] = UNSET
    json: Union[Unset, "NatsOrganizationJson"] = UNSET
    jetstream_enabled: Union[Unset, bool] = UNSET
    jetstream_max_mem: Union[Unset, str] = UNSET
    jetstream_max_file: Union[Unset, str] = UNSET
    jetstream_max_streams: Union[Unset, int] = UNSET
    jetstream_max_consumers: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        created = self.created.isoformat()

        modified = self.modified.isoformat()

        slug = self.slug
        imports = self.imports

        exports = self.exports

        users = self.users

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
                "id": id,
                "name": name,
                "created": created,
                "modified": modified,
                "slug": slug,
                "imports": imports,
                "exports": exports,
                "users": users,
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
        from ..models.nats_organization_json import NatsOrganizationJson

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        slug = d.pop("slug")

        imports = cast(List[int], d.pop("imports"))

        exports = cast(List[int], d.pop("exports"))

        users = cast(List[int], d.pop("users"))

        is_active = d.pop("is_active", UNSET)

        _json = d.pop("json", UNSET)
        json: Union[Unset, NatsOrganizationJson]
        if isinstance(_json, Unset):
            json = UNSET
        else:
            json = NatsOrganizationJson.from_dict(_json)

        jetstream_enabled = d.pop("jetstream_enabled", UNSET)

        jetstream_max_mem = d.pop("jetstream_max_mem", UNSET)

        jetstream_max_file = d.pop("jetstream_max_file", UNSET)

        jetstream_max_streams = d.pop("jetstream_max_streams", UNSET)

        jetstream_max_consumers = d.pop("jetstream_max_consumers", UNSET)

        nats_organization = cls(
            id=id,
            name=name,
            created=created,
            modified=modified,
            slug=slug,
            imports=imports,
            exports=exports,
            users=users,
            is_active=is_active,
            json=json,
            jetstream_enabled=jetstream_enabled,
            jetstream_max_mem=jetstream_max_mem,
            jetstream_max_file=jetstream_max_file,
            jetstream_max_streams=jetstream_max_streams,
            jetstream_max_consumers=jetstream_max_consumers,
        )

        nats_organization.additional_properties = d
        return nats_organization

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
