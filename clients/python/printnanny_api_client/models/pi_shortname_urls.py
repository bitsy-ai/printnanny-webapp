from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PiShortnameUrls")


@attr.s(auto_attribs=True)
class PiShortnameUrls:
    """
    Attributes:
        mission_control (str):
        octoprint (str):
        swupdate (str):
        syncthing (str):
    """

    mission_control: str
    octoprint: str
    swupdate: str
    syncthing: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mission_control = self.mission_control
        octoprint = self.octoprint
        swupdate = self.swupdate
        syncthing = self.syncthing

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mission_control": mission_control,
                "octoprint": octoprint,
                "swupdate": swupdate,
                "syncthing": syncthing,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mission_control = d.pop("mission_control")

        octoprint = d.pop("octoprint")

        swupdate = d.pop("swupdate")

        syncthing = d.pop("syncthing")

        pi_shortname_urls = cls(
            mission_control=mission_control,
            octoprint=octoprint,
            swupdate=swupdate,
            syncthing=syncthing,
        )

        pi_shortname_urls.additional_properties = d
        return pi_shortname_urls

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
