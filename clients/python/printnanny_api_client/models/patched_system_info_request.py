import json
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patched_system_info_request_os_release_json import PatchedSystemInfoRequestOsReleaseJson


T = TypeVar("T", bound="PatchedSystemInfoRequest")


@attr.s(auto_attribs=True)
class PatchedSystemInfoRequest:
    """
    Attributes:
        machine_id (Union[Unset, str]): Populated from /etc/machine-id
        revision (Union[Unset, str]): Populated from /proc/cpuinfo REVISION
        model (Union[Unset, str]): Populated from /proc/cpuinfo MODEL
        serial (Union[Unset, str]): Populated from /proc/cpuinfo SERIAL
        cores (Union[Unset, int]):
        ram (Union[Unset, int]):
        os_version_id (Union[Unset, str]): PrintNanny OS VERSION_ID from /etc/os-release
        os_build_id (Union[Unset, str]): PrintNanny OS BUILD_ID from /etc/os-release
        os_release_json (Union[Unset, PatchedSystemInfoRequestOsReleaseJson]): Full contents of /etc/os-release in
            key:value format
        uptime (Union[Unset, int]): system uptime (in seconds)
        rootfs_size (Union[Unset, int]): Size of /dev/root filesystem in bytes
        rootfs_used (Union[Unset, int]): Space used in /dev/root filesystem in bytes
        bootfs_size (Union[Unset, int]): Size of /dev/mmcblk0p1 filesystem in bytes
        bootfs_used (Union[Unset, int]): Space used in /dev/mmcblk0p1 filesystem in bytes
        datafs_size (Union[Unset, int]): Size of /dev/mmcblk0p4 filesystem in bytes
        datafs_used (Union[Unset, int]): Space used in /dev/mmcblk0p4 filesystem in bytes
        pi (Union[Unset, int]):
    """

    machine_id: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    serial: Union[Unset, str] = UNSET
    cores: Union[Unset, int] = UNSET
    ram: Union[Unset, int] = UNSET
    os_version_id: Union[Unset, str] = UNSET
    os_build_id: Union[Unset, str] = UNSET
    os_release_json: Union[Unset, "PatchedSystemInfoRequestOsReleaseJson"] = UNSET
    uptime: Union[Unset, int] = UNSET
    rootfs_size: Union[Unset, int] = UNSET
    rootfs_used: Union[Unset, int] = UNSET
    bootfs_size: Union[Unset, int] = UNSET
    bootfs_used: Union[Unset, int] = UNSET
    datafs_size: Union[Unset, int] = UNSET
    datafs_used: Union[Unset, int] = UNSET
    pi: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        machine_id = self.machine_id
        revision = self.revision
        model = self.model
        serial = self.serial
        cores = self.cores
        ram = self.ram
        os_version_id = self.os_version_id
        os_build_id = self.os_build_id
        os_release_json: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.os_release_json, Unset):
            os_release_json = self.os_release_json.to_dict()

        uptime = self.uptime
        rootfs_size = self.rootfs_size
        rootfs_used = self.rootfs_used
        bootfs_size = self.bootfs_size
        bootfs_used = self.bootfs_used
        datafs_size = self.datafs_size
        datafs_used = self.datafs_used
        pi = self.pi

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if machine_id is not UNSET:
            field_dict["machine_id"] = machine_id
        if revision is not UNSET:
            field_dict["revision"] = revision
        if model is not UNSET:
            field_dict["model"] = model
        if serial is not UNSET:
            field_dict["serial"] = serial
        if cores is not UNSET:
            field_dict["cores"] = cores
        if ram is not UNSET:
            field_dict["ram"] = ram
        if os_version_id is not UNSET:
            field_dict["os_version_id"] = os_version_id
        if os_build_id is not UNSET:
            field_dict["os_build_id"] = os_build_id
        if os_release_json is not UNSET:
            field_dict["os_release_json"] = os_release_json
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if rootfs_size is not UNSET:
            field_dict["rootfs_size"] = rootfs_size
        if rootfs_used is not UNSET:
            field_dict["rootfs_used"] = rootfs_used
        if bootfs_size is not UNSET:
            field_dict["bootfs_size"] = bootfs_size
        if bootfs_used is not UNSET:
            field_dict["bootfs_used"] = bootfs_used
        if datafs_size is not UNSET:
            field_dict["datafs_size"] = datafs_size
        if datafs_used is not UNSET:
            field_dict["datafs_used"] = datafs_used
        if pi is not UNSET:
            field_dict["pi"] = pi

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

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if machine_id is not UNSET:
            field_dict["machine_id"] = machine_id
        if revision is not UNSET:
            field_dict["revision"] = revision
        if model is not UNSET:
            field_dict["model"] = model
        if serial is not UNSET:
            field_dict["serial"] = serial
        if cores is not UNSET:
            field_dict["cores"] = cores
        if ram is not UNSET:
            field_dict["ram"] = ram
        if os_version_id is not UNSET:
            field_dict["os_version_id"] = os_version_id
        if os_build_id is not UNSET:
            field_dict["os_build_id"] = os_build_id
        if os_release_json is not UNSET:
            field_dict["os_release_json"] = os_release_json
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if rootfs_size is not UNSET:
            field_dict["rootfs_size"] = rootfs_size
        if rootfs_used is not UNSET:
            field_dict["rootfs_used"] = rootfs_used
        if bootfs_size is not UNSET:
            field_dict["bootfs_size"] = bootfs_size
        if bootfs_used is not UNSET:
            field_dict["bootfs_used"] = bootfs_used
        if datafs_size is not UNSET:
            field_dict["datafs_size"] = datafs_size
        if datafs_used is not UNSET:
            field_dict["datafs_used"] = datafs_used
        if pi is not UNSET:
            field_dict["pi"] = pi

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patched_system_info_request_os_release_json import PatchedSystemInfoRequestOsReleaseJson

        d = src_dict.copy()
        machine_id = d.pop("machine_id", UNSET)

        revision = d.pop("revision", UNSET)

        model = d.pop("model", UNSET)

        serial = d.pop("serial", UNSET)

        cores = d.pop("cores", UNSET)

        ram = d.pop("ram", UNSET)

        os_version_id = d.pop("os_version_id", UNSET)

        os_build_id = d.pop("os_build_id", UNSET)

        _os_release_json = d.pop("os_release_json", UNSET)
        os_release_json: Union[Unset, PatchedSystemInfoRequestOsReleaseJson]
        if isinstance(_os_release_json, Unset):
            os_release_json = UNSET
        else:
            os_release_json = PatchedSystemInfoRequestOsReleaseJson.from_dict(_os_release_json)

        uptime = d.pop("uptime", UNSET)

        rootfs_size = d.pop("rootfs_size", UNSET)

        rootfs_used = d.pop("rootfs_used", UNSET)

        bootfs_size = d.pop("bootfs_size", UNSET)

        bootfs_used = d.pop("bootfs_used", UNSET)

        datafs_size = d.pop("datafs_size", UNSET)

        datafs_used = d.pop("datafs_used", UNSET)

        pi = d.pop("pi", UNSET)

        patched_system_info_request = cls(
            machine_id=machine_id,
            revision=revision,
            model=model,
            serial=serial,
            cores=cores,
            ram=ram,
            os_version_id=os_version_id,
            os_build_id=os_build_id,
            os_release_json=os_release_json,
            uptime=uptime,
            rootfs_size=rootfs_size,
            rootfs_used=rootfs_used,
            bootfs_size=bootfs_size,
            bootfs_used=bootfs_used,
            datafs_size=datafs_size,
            datafs_used=datafs_used,
            pi=pi,
        )

        patched_system_info_request.additional_properties = d
        return patched_system_info_request

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
