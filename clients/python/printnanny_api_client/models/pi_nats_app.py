from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nats_organization import NatsOrganization
    from ..models.pi_nats_app_json import PiNatsAppJson


T = TypeVar("T", bound="PiNatsApp")


@attr.s(auto_attribs=True)
class PiNatsApp:
    """
    Attributes:
        id (int):
        pi (int):
        organization (NatsOrganization):
        organization_user (int):
        nats_server_uri (str):
        nats_ws_uri (str):
        nats_subject_pattern (str):
        nats_subject_pattern_template (str):
        mqtt_subject_template_moonraker_request (str):
        mqtt_subject_moonraker_request (str):
        mqtt_subject_template_moonraker_response (str):
        mqtt_subject_moonraker_response (str):
        mqtt_subject_template_klipper_status (str):
        mqtt_subject_klipper_status (str):
        mqtt_broker_host (str):
        mqtt_broker_port (int):
        app_name (Union[Unset, str]):
        json (Union[Unset, PiNatsAppJson]): Output of `nsc describe account`
    """

    id: int
    pi: int
    organization: "NatsOrganization"
    organization_user: int
    nats_server_uri: str
    nats_ws_uri: str
    nats_subject_pattern: str
    nats_subject_pattern_template: str
    mqtt_subject_template_moonraker_request: str
    mqtt_subject_moonraker_request: str
    mqtt_subject_template_moonraker_response: str
    mqtt_subject_moonraker_response: str
    mqtt_subject_template_klipper_status: str
    mqtt_subject_klipper_status: str
    mqtt_broker_host: str
    mqtt_broker_port: int
    app_name: Union[Unset, str] = UNSET
    json: Union[Unset, "PiNatsAppJson"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        pi = self.pi
        organization = self.organization.to_dict()

        organization_user = self.organization_user
        nats_server_uri = self.nats_server_uri
        nats_ws_uri = self.nats_ws_uri
        nats_subject_pattern = self.nats_subject_pattern
        nats_subject_pattern_template = self.nats_subject_pattern_template
        mqtt_subject_template_moonraker_request = self.mqtt_subject_template_moonraker_request
        mqtt_subject_moonraker_request = self.mqtt_subject_moonraker_request
        mqtt_subject_template_moonraker_response = self.mqtt_subject_template_moonraker_response
        mqtt_subject_moonraker_response = self.mqtt_subject_moonraker_response
        mqtt_subject_template_klipper_status = self.mqtt_subject_template_klipper_status
        mqtt_subject_klipper_status = self.mqtt_subject_klipper_status
        mqtt_broker_host = self.mqtt_broker_host
        mqtt_broker_port = self.mqtt_broker_port
        app_name = self.app_name
        json: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.json, Unset):
            json = self.json.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "pi": pi,
                "organization": organization,
                "organization_user": organization_user,
                "nats_server_uri": nats_server_uri,
                "nats_ws_uri": nats_ws_uri,
                "nats_subject_pattern": nats_subject_pattern,
                "nats_subject_pattern_template": nats_subject_pattern_template,
                "mqtt_subject_template_moonraker_request": mqtt_subject_template_moonraker_request,
                "mqtt_subject_moonraker_request": mqtt_subject_moonraker_request,
                "mqtt_subject_template_moonraker_response": mqtt_subject_template_moonraker_response,
                "mqtt_subject_moonraker_response": mqtt_subject_moonraker_response,
                "mqtt_subject_template_klipper_status": mqtt_subject_template_klipper_status,
                "mqtt_subject_klipper_status": mqtt_subject_klipper_status,
                "mqtt_broker_host": mqtt_broker_host,
                "mqtt_broker_port": mqtt_broker_port,
            }
        )
        if app_name is not UNSET:
            field_dict["app_name"] = app_name
        if json is not UNSET:
            field_dict["json"] = json

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nats_organization import NatsOrganization
        from ..models.pi_nats_app_json import PiNatsAppJson

        d = src_dict.copy()
        id = d.pop("id")

        pi = d.pop("pi")

        organization = NatsOrganization.from_dict(d.pop("organization"))

        organization_user = d.pop("organization_user")

        nats_server_uri = d.pop("nats_server_uri")

        nats_ws_uri = d.pop("nats_ws_uri")

        nats_subject_pattern = d.pop("nats_subject_pattern")

        nats_subject_pattern_template = d.pop("nats_subject_pattern_template")

        mqtt_subject_template_moonraker_request = d.pop("mqtt_subject_template_moonraker_request")

        mqtt_subject_moonraker_request = d.pop("mqtt_subject_moonraker_request")

        mqtt_subject_template_moonraker_response = d.pop("mqtt_subject_template_moonraker_response")

        mqtt_subject_moonraker_response = d.pop("mqtt_subject_moonraker_response")

        mqtt_subject_template_klipper_status = d.pop("mqtt_subject_template_klipper_status")

        mqtt_subject_klipper_status = d.pop("mqtt_subject_klipper_status")

        mqtt_broker_host = d.pop("mqtt_broker_host")

        mqtt_broker_port = d.pop("mqtt_broker_port")

        app_name = d.pop("app_name", UNSET)

        _json = d.pop("json", UNSET)
        json: Union[Unset, PiNatsAppJson]
        if isinstance(_json, Unset):
            json = UNSET
        else:
            json = PiNatsAppJson.from_dict(_json)

        pi_nats_app = cls(
            id=id,
            pi=pi,
            organization=organization,
            organization_user=organization_user,
            nats_server_uri=nats_server_uri,
            nats_ws_uri=nats_ws_uri,
            nats_subject_pattern=nats_subject_pattern,
            nats_subject_pattern_template=nats_subject_pattern_template,
            mqtt_subject_template_moonraker_request=mqtt_subject_template_moonraker_request,
            mqtt_subject_moonraker_request=mqtt_subject_moonraker_request,
            mqtt_subject_template_moonraker_response=mqtt_subject_template_moonraker_response,
            mqtt_subject_moonraker_response=mqtt_subject_moonraker_response,
            mqtt_subject_template_klipper_status=mqtt_subject_template_klipper_status,
            mqtt_subject_klipper_status=mqtt_subject_klipper_status,
            mqtt_broker_host=mqtt_broker_host,
            mqtt_broker_port=mqtt_broker_port,
            app_name=app_name,
            json=json,
        )

        pi_nats_app.additional_properties = d
        return pi_nats_app

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
