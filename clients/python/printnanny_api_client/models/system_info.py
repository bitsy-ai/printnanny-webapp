import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.system_info_os_release_json import SystemInfoOsReleaseJson


T = TypeVar("T", bound="SystemInfo")


@attr.s(auto_attribs=True)
class SystemInfo:
    """
    Attributes:
        id (int):
        bootfs_available (int):
        bootfs_available_pretty (str):
        bootfs_used_pretty (str):
        bootfs_size_pretty (str):
        datafs_available (int):
        datafs_available_pretty (str):
        datafs_used_pretty (str):
        datafs_size_pretty (str):
        rootfs_available (int):
        rootfs_available_pretty (str):
        rootfs_size_pretty (str):
        rootfs_used_pretty (str):
        created_dt (datetime.datetime):
        updated_dt (datetime.datetime):
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
        os_release_json (Union[Unset, SystemInfoOsReleaseJson]): Full contents of /etc/os-release in key:value format
    """

    id: int
    bootfs_available: int
    bootfs_available_pretty: str
    bootfs_used_pretty: str
    bootfs_size_pretty: str
    datafs_available: int
    datafs_available_pretty: str
    datafs_used_pretty: str
    datafs_size_pretty: str
    rootfs_available: int
    rootfs_available_pretty: str
    rootfs_size_pretty: str
    rootfs_used_pretty: str
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
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
    os_release_json: Union[Unset, "SystemInfoOsReleaseJson"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        bootfs_available = self.bootfs_available
        bootfs_available_pretty = self.bootfs_available_pretty
        bootfs_used_pretty = self.bootfs_used_pretty
        bootfs_size_pretty = self.bootfs_size_pretty
        datafs_available = self.datafs_available
        datafs_available_pretty = self.datafs_available_pretty
        datafs_used_pretty = self.datafs_used_pretty
        datafs_size_pretty = self.datafs_size_pretty
        rootfs_available = self.rootfs_available
        rootfs_available_pretty = self.rootfs_available_pretty
        rootfs_size_pretty = self.rootfs_size_pretty
        rootfs_used_pretty = self.rootfs_used_pretty
        created_dt = self.created_dt.isoformat()

        updated_dt = self.updated_dt.isoformat()

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
                "id": id,
                "bootfs_available": bootfs_available,
                "bootfs_available_pretty": bootfs_available_pretty,
                "bootfs_used_pretty": bootfs_used_pretty,
                "bootfs_size_pretty": bootfs_size_pretty,
                "datafs_available": datafs_available,
                "datafs_available_pretty": datafs_available_pretty,
                "datafs_used_pretty": datafs_used_pretty,
                "datafs_size_pretty": datafs_size_pretty,
                "rootfs_available": rootfs_available,
                "rootfs_available_pretty": rootfs_available_pretty,
                "rootfs_size_pretty": rootfs_size_pretty,
                "rootfs_used_pretty": rootfs_used_pretty,
                "created_dt": created_dt,
                "updated_dt": updated_dt,
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
        from ..models.system_info_os_release_json import SystemInfoOsReleaseJson

        d = src_dict.copy()
        id = d.pop("id")

        bootfs_available = d.pop("bootfs_available")

        bootfs_available_pretty = d.pop("bootfs_available_pretty")

        bootfs_used_pretty = d.pop("bootfs_used_pretty")

        bootfs_size_pretty = d.pop("bootfs_size_pretty")

        datafs_available = d.pop("datafs_available")

        datafs_available_pretty = d.pop("datafs_available_pretty")

        datafs_used_pretty = d.pop("datafs_used_pretty")

        datafs_size_pretty = d.pop("datafs_size_pretty")

        rootfs_available = d.pop("rootfs_available")

        rootfs_available_pretty = d.pop("rootfs_available_pretty")

        rootfs_size_pretty = d.pop("rootfs_size_pretty")

        rootfs_used_pretty = d.pop("rootfs_used_pretty")

        created_dt = isoparse(d.pop("created_dt"))

        updated_dt = isoparse(d.pop("updated_dt"))

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
        os_release_json: Union[Unset, SystemInfoOsReleaseJson]
        if isinstance(_os_release_json, Unset):
            os_release_json = UNSET
        else:
            os_release_json = SystemInfoOsReleaseJson.from_dict(_os_release_json)

        system_info = cls(
            id=id,
            bootfs_available=bootfs_available,
            bootfs_available_pretty=bootfs_available_pretty,
            bootfs_used_pretty=bootfs_used_pretty,
            bootfs_size_pretty=bootfs_size_pretty,
            datafs_available=datafs_available,
            datafs_available_pretty=datafs_available_pretty,
            datafs_used_pretty=datafs_used_pretty,
            datafs_size_pretty=datafs_size_pretty,
            rootfs_available=rootfs_available,
            rootfs_available_pretty=rootfs_available_pretty,
            rootfs_size_pretty=rootfs_size_pretty,
            rootfs_used_pretty=rootfs_used_pretty,
            created_dt=created_dt,
            updated_dt=updated_dt,
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

        system_info.additional_properties = d
        return system_info

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
