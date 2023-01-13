from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedOctoPrintSettingsRequest")


@attr.s(auto_attribs=True)
class PatchedOctoPrintSettingsRequest:
    """
    Attributes:
        octoprint_enabled (Union[Unset, bool]): Start OctoPrint service
        events_enabled (Union[Unset, bool]): Send OctoPrint events related to print job status/progress to PrintNanny
            Cloud https://docs.octoprint.org/en/master/events/index.html
        sync_gcode (Union[Unset, bool]): Sync Gcode files to/from PrintNanny Cloud
        sync_printer_profiles (Union[Unset, bool]): Sync Printer Profiles to/from PrintNanny Cloud
        sync_backups (Union[Unset, bool]): Upload OctoPrint backups to PrintNanny Cloud
        auto_backup (Union[Unset, str]):
        octoprint_server (Union[Unset, int]):
    """

    octoprint_enabled: Union[Unset, bool] = UNSET
    events_enabled: Union[Unset, bool] = UNSET
    sync_gcode: Union[Unset, bool] = UNSET
    sync_printer_profiles: Union[Unset, bool] = UNSET
    sync_backups: Union[Unset, bool] = UNSET
    auto_backup: Union[Unset, str] = UNSET
    octoprint_server: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        octoprint_enabled = self.octoprint_enabled
        events_enabled = self.events_enabled
        sync_gcode = self.sync_gcode
        sync_printer_profiles = self.sync_printer_profiles
        sync_backups = self.sync_backups
        auto_backup = self.auto_backup
        octoprint_server = self.octoprint_server

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if octoprint_enabled is not UNSET:
            field_dict["octoprint_enabled"] = octoprint_enabled
        if events_enabled is not UNSET:
            field_dict["events_enabled"] = events_enabled
        if sync_gcode is not UNSET:
            field_dict["sync_gcode"] = sync_gcode
        if sync_printer_profiles is not UNSET:
            field_dict["sync_printer_profiles"] = sync_printer_profiles
        if sync_backups is not UNSET:
            field_dict["sync_backups"] = sync_backups
        if auto_backup is not UNSET:
            field_dict["auto_backup"] = auto_backup
        if octoprint_server is not UNSET:
            field_dict["octoprint_server"] = octoprint_server

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        octoprint_enabled = (
            self.octoprint_enabled
            if isinstance(self.octoprint_enabled, Unset)
            else (None, str(self.octoprint_enabled).encode(), "text/plain")
        )
        events_enabled = (
            self.events_enabled
            if isinstance(self.events_enabled, Unset)
            else (None, str(self.events_enabled).encode(), "text/plain")
        )
        sync_gcode = (
            self.sync_gcode
            if isinstance(self.sync_gcode, Unset)
            else (None, str(self.sync_gcode).encode(), "text/plain")
        )
        sync_printer_profiles = (
            self.sync_printer_profiles
            if isinstance(self.sync_printer_profiles, Unset)
            else (None, str(self.sync_printer_profiles).encode(), "text/plain")
        )
        sync_backups = (
            self.sync_backups
            if isinstance(self.sync_backups, Unset)
            else (None, str(self.sync_backups).encode(), "text/plain")
        )
        auto_backup = (
            self.auto_backup
            if isinstance(self.auto_backup, Unset)
            else (None, str(self.auto_backup).encode(), "text/plain")
        )
        octoprint_server = (
            self.octoprint_server
            if isinstance(self.octoprint_server, Unset)
            else (None, str(self.octoprint_server).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if octoprint_enabled is not UNSET:
            field_dict["octoprint_enabled"] = octoprint_enabled
        if events_enabled is not UNSET:
            field_dict["events_enabled"] = events_enabled
        if sync_gcode is not UNSET:
            field_dict["sync_gcode"] = sync_gcode
        if sync_printer_profiles is not UNSET:
            field_dict["sync_printer_profiles"] = sync_printer_profiles
        if sync_backups is not UNSET:
            field_dict["sync_backups"] = sync_backups
        if auto_backup is not UNSET:
            field_dict["auto_backup"] = auto_backup
        if octoprint_server is not UNSET:
            field_dict["octoprint_server"] = octoprint_server

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        octoprint_enabled = d.pop("octoprint_enabled", UNSET)

        events_enabled = d.pop("events_enabled", UNSET)

        sync_gcode = d.pop("sync_gcode", UNSET)

        sync_printer_profiles = d.pop("sync_printer_profiles", UNSET)

        sync_backups = d.pop("sync_backups", UNSET)

        auto_backup = d.pop("auto_backup", UNSET)

        octoprint_server = d.pop("octoprint_server", UNSET)

        patched_octo_print_settings_request = cls(
            octoprint_enabled=octoprint_enabled,
            events_enabled=events_enabled,
            sync_gcode=sync_gcode,
            sync_printer_profiles=sync_printer_profiles,
            sync_backups=sync_backups,
            auto_backup=auto_backup,
            octoprint_server=octoprint_server,
        )

        patched_octo_print_settings_request.additional_properties = d
        return patched_octo_print_settings_request

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
