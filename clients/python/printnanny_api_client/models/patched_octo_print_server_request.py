from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedOctoPrintServerRequest")


@attr.s(auto_attribs=True)
class PatchedOctoPrintServerRequest:
    """
    Attributes:
        base_path (Union[Unset, str]):
        venv_path (Union[Unset, str]):
        pip_path (Union[Unset, str]):
        python_path (Union[Unset, str]):
        octoprint_version (Union[Unset, str]):
        pip_version (Union[Unset, str]):
        python_version (Union[Unset, str]):
        printnanny_plugin_version (Union[Unset, str]):
        api_key (Union[Unset, None, str]):
        pi (Union[Unset, int]):
    """

    base_path: Union[Unset, str] = UNSET
    venv_path: Union[Unset, str] = UNSET
    pip_path: Union[Unset, str] = UNSET
    python_path: Union[Unset, str] = UNSET
    octoprint_version: Union[Unset, str] = UNSET
    pip_version: Union[Unset, str] = UNSET
    python_version: Union[Unset, str] = UNSET
    printnanny_plugin_version: Union[Unset, str] = UNSET
    api_key: Union[Unset, None, str] = UNSET
    pi: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        base_path = self.base_path
        venv_path = self.venv_path
        pip_path = self.pip_path
        python_path = self.python_path
        octoprint_version = self.octoprint_version
        pip_version = self.pip_version
        python_version = self.python_version
        printnanny_plugin_version = self.printnanny_plugin_version
        api_key = self.api_key
        pi = self.pi

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_path is not UNSET:
            field_dict["base_path"] = base_path
        if venv_path is not UNSET:
            field_dict["venv_path"] = venv_path
        if pip_path is not UNSET:
            field_dict["pip_path"] = pip_path
        if python_path is not UNSET:
            field_dict["python_path"] = python_path
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
        if pi is not UNSET:
            field_dict["pi"] = pi

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        base_path = (
            self.base_path if isinstance(self.base_path, Unset) else (None, str(self.base_path).encode(), "text/plain")
        )
        venv_path = (
            self.venv_path if isinstance(self.venv_path, Unset) else (None, str(self.venv_path).encode(), "text/plain")
        )
        pip_path = (
            self.pip_path if isinstance(self.pip_path, Unset) else (None, str(self.pip_path).encode(), "text/plain")
        )
        python_path = (
            self.python_path
            if isinstance(self.python_path, Unset)
            else (None, str(self.python_path).encode(), "text/plain")
        )
        octoprint_version = (
            self.octoprint_version
            if isinstance(self.octoprint_version, Unset)
            else (None, str(self.octoprint_version).encode(), "text/plain")
        )
        pip_version = (
            self.pip_version
            if isinstance(self.pip_version, Unset)
            else (None, str(self.pip_version).encode(), "text/plain")
        )
        python_version = (
            self.python_version
            if isinstance(self.python_version, Unset)
            else (None, str(self.python_version).encode(), "text/plain")
        )
        printnanny_plugin_version = (
            self.printnanny_plugin_version
            if isinstance(self.printnanny_plugin_version, Unset)
            else (None, str(self.printnanny_plugin_version).encode(), "text/plain")
        )
        api_key = self.api_key if isinstance(self.api_key, Unset) else (None, str(self.api_key).encode(), "text/plain")
        pi = self.pi if isinstance(self.pi, Unset) else (None, str(self.pi).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if base_path is not UNSET:
            field_dict["base_path"] = base_path
        if venv_path is not UNSET:
            field_dict["venv_path"] = venv_path
        if pip_path is not UNSET:
            field_dict["pip_path"] = pip_path
        if python_path is not UNSET:
            field_dict["python_path"] = python_path
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
        if pi is not UNSET:
            field_dict["pi"] = pi

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        base_path = d.pop("base_path", UNSET)

        venv_path = d.pop("venv_path", UNSET)

        pip_path = d.pop("pip_path", UNSET)

        python_path = d.pop("python_path", UNSET)

        octoprint_version = d.pop("octoprint_version", UNSET)

        pip_version = d.pop("pip_version", UNSET)

        python_version = d.pop("python_version", UNSET)

        printnanny_plugin_version = d.pop("printnanny_plugin_version", UNSET)

        api_key = d.pop("api_key", UNSET)

        pi = d.pop("pi", UNSET)

        patched_octo_print_server_request = cls(
            base_path=base_path,
            venv_path=venv_path,
            pip_path=pip_path,
            python_path=python_path,
            octoprint_version=octoprint_version,
            pip_version=pip_version,
            python_version=python_version,
            printnanny_plugin_version=printnanny_plugin_version,
            api_key=api_key,
            pi=pi,
        )

        patched_octo_print_server_request.additional_properties = d
        return patched_octo_print_server_request

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
