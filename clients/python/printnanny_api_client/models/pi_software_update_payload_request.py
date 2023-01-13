from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PiSoftwareUpdatePayloadRequest")


@attr.s(auto_attribs=True)
class PiSoftwareUpdatePayloadRequest:
    """
    Attributes:
        wic_tarball_url (str):
        wic_bmap_url (str):
        manifest_url (str):
        swu_url (str):
        version_id (str):
        version (str):
        version_codename (str):
    """

    wic_tarball_url: str
    wic_bmap_url: str
    manifest_url: str
    swu_url: str
    version_id: str
    version: str
    version_codename: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        wic_tarball_url = self.wic_tarball_url
        wic_bmap_url = self.wic_bmap_url
        manifest_url = self.manifest_url
        swu_url = self.swu_url
        version_id = self.version_id
        version = self.version
        version_codename = self.version_codename

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "wic_tarball_url": wic_tarball_url,
                "wic_bmap_url": wic_bmap_url,
                "manifest_url": manifest_url,
                "swu_url": swu_url,
                "version_id": version_id,
                "version": version,
                "version_codename": version_codename,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        wic_tarball_url = d.pop("wic_tarball_url")

        wic_bmap_url = d.pop("wic_bmap_url")

        manifest_url = d.pop("manifest_url")

        swu_url = d.pop("swu_url")

        version_id = d.pop("version_id")

        version = d.pop("version")

        version_codename = d.pop("version_codename")

        pi_software_update_payload_request = cls(
            wic_tarball_url=wic_tarball_url,
            wic_bmap_url=wic_bmap_url,
            manifest_url=manifest_url,
            swu_url=swu_url,
            version_id=version_id,
            version=version,
            version_codename=version_codename,
        )

        pi_software_update_payload_request.additional_properties = d
        return pi_software_update_payload_request

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
