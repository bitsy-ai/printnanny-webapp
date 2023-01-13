import json
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.system_info_request_os_release_json import SystemInfoRequestOsReleaseJson


T = TypeVar("T", bound="SystemInfoRequest")


@attr.s(auto_attribs=True)
class SystemInfoRequest:
    """
    Attributes:
        machine_id (str): Populated from /etc/machine-id
        revision (str): Populated from /proc/cpuinfo REVISION
        model (str): Populated from /proc/cpuinfo MODEL
        serial (str): Populated from /proc/cpuinfo SERIAL
        cores (int):
        ram (int):
        uptime (int): system uptime (in seconds)
        rootfs_size (int): Size of /dev/root filesystem in bytes
        rootfs_used (int): Space used in /dev/root filesystem in bytes
        bootfs_size (int): Size of /dev/mmcblk0p1 filesystem in bytes
        bootfs_used (int): Space used in /dev/mmcblk0p1 filesystem in bytes
        datafs_size (int): Size of /dev/mmcblk0p4 filesystem in bytes
        datafs_used (int): Space used in /dev/mmcblk0p4 filesystem in bytes
        pi (int):
        os_version_id (Union[Unset, str]): PrintNanny OS VERSION_ID from /etc/os-release
        os_build_id (Union[Unset, str]): PrintNanny OS BUILD_ID from /etc/os-release
        os_release_json (Union[Unset, SystemInfoRequestOsReleaseJson]): Full contents of /etc/os-release in key:value
            format
    """

    machine_id: str
    revision: str
    model: str
    serial: str
    cores: int
    ram: int
    uptime: int
    rootfs_size: int
    rootfs_used: int
    bootfs_size: int
    bootfs_used: int
    datafs_size: int
    datafs_used: int
    pi: int
    os_version_id: Union[Unset, str] = UNSET
    os_build_id: Union[Unset, str] = UNSET
    os_release_json: Union[Unset, "SystemInfoRequestOsReleaseJson"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        machine_id = self.machine_id
        revision = self.revision
        model = self.model
        serial = self.serial
        cores = self.cores
        ram = self.ram
        uptime = self.uptime
        rootfs_size = self.rootfs_size
        rootfs_used = self.rootfs_used
        bootfs_size = self.bootfs_size
        bootfs_used = self.bootfs_used
        datafs_size = self.datafs_size
        datafs_used = self.datafs_used
        pi = self.pi
        os_version_id = self.os_version_id
        os_build_id = self.os_build_id
        os_release_json: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.os_release_json, Unset):
            os_release_json = self.os_release_json.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "machine_id": machine_id,
                "revision": revision,
                "model": model,
                "serial": serial,
                "cores": cores,
                "ram": ram,
                "uptime": uptime,
                "rootfs_size": rootfs_size,
                "rootfs_used": rootfs_used,
                "bootfs_size": bootfs_size,
                "bootfs_used": bootfs_used,
                "datafs_size": datafs_size,
                "datafs_used": datafs_used,
                "pi": pi,
            }
        )
        if os_version_id is not UNSET:
            field_dict["os_version_id"] = os_version_id
        if os_build_id is not UNSET:
            field_dict["os_build_id"] = os_build_id
        if os_release_json is not UNSET:
            field_dict["os_release_json"] = os_release_json

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        machine_id = (
            self.machine_id
            if isinstance(self.machine_id, Unset)
            else (None, str(self.machine_id).encode(), "text/plain")
        )
        revision = (
            self.revision if isinstance(self.revision, Unset) else (None, str(self.revision).encode(), "text/plain")
        )
        model = self.model if isinstance(self.model, Unset) else (None, str(self.model).encode(), "text/plain")
        serial = self.serial if isinstance(self.serial, Unset) else (None, str(self.serial).encode(), "text/plain")
        cores = self.cores if isinstance(self.cores, Unset) else (None, str(self.cores).encode(), "text/plain")
        ram = self.ram if isinstance(self.ram, Unset) else (None, str(self.ram).encode(), "text/plain")
        uptime = self.uptime if isinstance(self.uptime, Unset) else (None, str(self.uptime).encode(), "text/plain")
        rootfs_size = (
            self.rootfs_size
            if isinstance(self.rootfs_size, Unset)
            else (None, str(self.rootfs_size).encode(), "text/plain")
        )
        rootfs_used = (
            self.rootfs_used
            if isinstance(self.rootfs_used, Unset)
            else (None, str(self.rootfs_used).encode(), "text/plain")
        )
        bootfs_size = (
            self.bootfs_size
            if isinstance(self.bootfs_size, Unset)
            else (None, str(self.bootfs_size).encode(), "text/plain")
        )
        bootfs_used = (
            self.bootfs_used
            if isinstance(self.bootfs_used, Unset)
            else (None, str(self.bootfs_used).encode(), "text/plain")
        )
        datafs_size = (
            self.datafs_size
            if isinstance(self.datafs_size, Unset)
            else (None, str(self.datafs_size).encode(), "text/plain")
        )
        datafs_used = (
            self.datafs_used
            if isinstance(self.datafs_used, Unset)
            else (None, str(self.datafs_used).encode(), "text/plain")
        )
        pi = self.pi if isinstance(self.pi, Unset) else (None, str(self.pi).encode(), "text/plain")
        os_version_id = (
            self.os_version_id
            if isinstance(self.os_version_id, Unset)
            else (None, str(self.os_version_id).encode(), "text/plain")
        )
        os_build_id = (
            self.os_build_id
            if isinstance(self.os_build_id, Unset)
            else (None, str(self.os_build_id).encode(), "text/plain")
        )
        os_release_json: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.os_release_json, Unset):
            os_release_json = (None, json.dumps(self.os_release_json.to_dict()).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "machine_id": machine_id,
                "revision": revision,
                "model": model,
                "serial": serial,
                "cores": cores,
                "ram": ram,
                "uptime": uptime,
                "rootfs_size": rootfs_size,
                "rootfs_used": rootfs_used,
                "bootfs_size": bootfs_size,
                "bootfs_used": bootfs_used,
                "datafs_size": datafs_size,
                "datafs_used": datafs_used,
                "pi": pi,
            }
        )
        if os_version_id is not UNSET:
            field_dict["os_version_id"] = os_version_id
        if os_build_id is not UNSET:
            field_dict["os_build_id"] = os_build_id
        if os_release_json is not UNSET:
            field_dict["os_release_json"] = os_release_json

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.system_info_request_os_release_json import SystemInfoRequestOsReleaseJson

        d = src_dict.copy()
        machine_id = d.pop("machine_id")

        revision = d.pop("revision")

        model = d.pop("model")

        serial = d.pop("serial")

        cores = d.pop("cores")

        ram = d.pop("ram")

        uptime = d.pop("uptime")

        rootfs_size = d.pop("rootfs_size")

        rootfs_used = d.pop("rootfs_used")

        bootfs_size = d.pop("bootfs_size")

        bootfs_used = d.pop("bootfs_used")

        datafs_size = d.pop("datafs_size")

        datafs_used = d.pop("datafs_used")

        pi = d.pop("pi")

        os_version_id = d.pop("os_version_id", UNSET)

        os_build_id = d.pop("os_build_id", UNSET)

        _os_release_json = d.pop("os_release_json", UNSET)
        os_release_json: Union[Unset, SystemInfoRequestOsReleaseJson]
        if isinstance(_os_release_json, Unset):
            os_release_json = UNSET
        else:
            os_release_json = SystemInfoRequestOsReleaseJson.from_dict(_os_release_json)

        system_info_request = cls(
            machine_id=machine_id,
            revision=revision,
            model=model,
            serial=serial,
            cores=cores,
            ram=ram,
            uptime=uptime,
            rootfs_size=rootfs_size,
            rootfs_used=rootfs_used,
            bootfs_size=bootfs_size,
            bootfs_used=bootfs_used,
            datafs_size=datafs_size,
            datafs_used=datafs_used,
            pi=pi,
            os_version_id=os_version_id,
            os_build_id=os_build_id,
            os_release_json=os_release_json,
        )

        system_info_request.additional_properties = d
        return system_info_request

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
