import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.octo_print_settings import OctoPrintSettings


T = TypeVar("T", bound="OctoPrintServer")


@attr.s(auto_attribs=True)
class OctoPrintServer:
    """
    Attributes:
        id (int):
        settings (OctoPrintSettings):
        base_path (str):
        venv_path (str):
        pip_path (str):
        python_path (str):
        created_dt (datetime.datetime):
        updated_dt (datetime.datetime):
        user (int):
        pi (int):
        octoprint_version (Union[Unset, str]):
        pip_version (Union[Unset, str]):
        python_version (Union[Unset, str]):
        printnanny_plugin_version (Union[Unset, str]):
        api_key (Union[Unset, None, str]):
    """

    id: int
    settings: "OctoPrintSettings"
    base_path: str
    venv_path: str
    pip_path: str
    python_path: str
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    user: int
    pi: int
    octoprint_version: Union[Unset, str] = UNSET
    pip_version: Union[Unset, str] = UNSET
    python_version: Union[Unset, str] = UNSET
    printnanny_plugin_version: Union[Unset, str] = UNSET
    api_key: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        settings = self.settings.to_dict()

        base_path = self.base_path
        venv_path = self.venv_path
        pip_path = self.pip_path
        python_path = self.python_path
        created_dt = self.created_dt.isoformat()

        updated_dt = self.updated_dt.isoformat()

        user = self.user
        pi = self.pi
        octoprint_version = self.octoprint_version
        pip_version = self.pip_version
        python_version = self.python_version
        printnanny_plugin_version = self.printnanny_plugin_version
        api_key = self.api_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "settings": settings,
                "base_path": base_path,
                "venv_path": venv_path,
                "pip_path": pip_path,
                "python_path": python_path,
                "created_dt": created_dt,
                "updated_dt": updated_dt,
                "user": user,
                "pi": pi,
            }
        )
        if octoprint_version is not UNSET:
            field_dict["octoprint_version"] = octoprint_version
        if pip_version is not UNSET:
            field_dict["pip_version"] = pip_version
        if python_version is not UNSET:
            field_dict["python_version"] = python_version
        if printnanny_plugin_version is not UNSET:
            field_dict["printnanny_plugin_version"] = printnanny_plugin_version
        if api_key is not UNSET:
            field_dict["api_key"] = api_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.octo_print_settings import OctoPrintSettings

        d = src_dict.copy()
        id = d.pop("id")

        settings = OctoPrintSettings.from_dict(d.pop("settings"))

        base_path = d.pop("base_path")

        venv_path = d.pop("venv_path")

        pip_path = d.pop("pip_path")

        python_path = d.pop("python_path")

        created_dt = isoparse(d.pop("created_dt"))

        updated_dt = isoparse(d.pop("updated_dt"))

        user = d.pop("user")

        pi = d.pop("pi")

        octoprint_version = d.pop("octoprint_version", UNSET)

        pip_version = d.pop("pip_version", UNSET)

        python_version = d.pop("python_version", UNSET)

        printnanny_plugin_version = d.pop("printnanny_plugin_version", UNSET)

        api_key = d.pop("api_key", UNSET)

        octo_print_server = cls(
            id=id,
            settings=settings,
            base_path=base_path,
            venv_path=venv_path,
            pip_path=pip_path,
            python_path=python_path,
            created_dt=created_dt,
            updated_dt=updated_dt,
            user=user,
            pi=pi,
            octoprint_version=octoprint_version,
            pip_version=pip_version,
            python_version=python_version,
            printnanny_plugin_version=printnanny_plugin_version,
            api_key=api_key,
        )

        octo_print_server.additional_properties = d
        return octo_print_server

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
