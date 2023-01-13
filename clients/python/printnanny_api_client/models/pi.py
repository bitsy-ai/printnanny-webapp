import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.sbc_enum import SbcEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.network_settings import NetworkSettings
    from ..models.octo_print_server import OctoPrintServer
    from ..models.pi_mdns_urls import PiMdnsUrls
    from ..models.pi_nats_app import PiNatsApp
    from ..models.pi_shortname_urls import PiShortnameUrls
    from ..models.pi_urls import PiUrls
    from ..models.system_info import SystemInfo
    from ..models.user import User
    from ..models.webrtc_stream import WebrtcStream


T = TypeVar("T", bound="Pi")


@attr.s(auto_attribs=True)
class Pi:
    """
    Attributes:
        id (int):
        network_settings (NetworkSettings):
        user (User):
        system_info (SystemInfo):
        webrtc_edge (WebrtcStream):
        webrtc_cloud (WebrtcStream):
        octoprint_server (OctoPrintServer):
        nats_app (PiNatsApp):
        urls (PiUrls):
        shortname_urls (PiShortnameUrls):
        mdns_urls (PiMdnsUrls):
        created_dt (datetime.datetime):
        last_boot (Optional[str]):
        sbc (Union[Unset, SbcEnum]):
        hostname (Union[Unset, str]): Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options
            menu (without .local extension)
        favorite (Union[Unset, bool]):
        setup_finished (Union[Unset, bool]):
    """

    id: int
    network_settings: "NetworkSettings"
    user: "User"
    system_info: "SystemInfo"
    webrtc_edge: "WebrtcStream"
    webrtc_cloud: "WebrtcStream"
    octoprint_server: "OctoPrintServer"
    nats_app: "PiNatsApp"
    urls: "PiUrls"
    shortname_urls: "PiShortnameUrls"
    mdns_urls: "PiMdnsUrls"
    created_dt: datetime.datetime
    last_boot: Optional[str]
    sbc: Union[Unset, SbcEnum] = UNSET
    hostname: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    setup_finished: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        network_settings = self.network_settings.to_dict()

        user = self.user.to_dict()

        system_info = self.system_info.to_dict()

        webrtc_edge = self.webrtc_edge.to_dict()

        webrtc_cloud = self.webrtc_cloud.to_dict()

        octoprint_server = self.octoprint_server.to_dict()

        nats_app = self.nats_app.to_dict()

        urls = self.urls.to_dict()

        shortname_urls = self.shortname_urls.to_dict()

        mdns_urls = self.mdns_urls.to_dict()

        created_dt = self.created_dt.isoformat()

        last_boot = self.last_boot
        sbc: Union[Unset, str] = UNSET
        if not isinstance(self.sbc, Unset):
            sbc = self.sbc.value

        hostname = self.hostname
        favorite = self.favorite
        setup_finished = self.setup_finished

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "network_settings": network_settings,
                "user": user,
                "system_info": system_info,
                "webrtc_edge": webrtc_edge,
                "webrtc_cloud": webrtc_cloud,
                "octoprint_server": octoprint_server,
                "nats_app": nats_app,
                "urls": urls,
                "shortname_urls": shortname_urls,
                "mdns_urls": mdns_urls,
                "created_dt": created_dt,
                "last_boot": last_boot,
            }
        )
        if sbc is not UNSET:
            field_dict["sbc"] = sbc
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if setup_finished is not UNSET:
            field_dict["setup_finished"] = setup_finished

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.network_settings import NetworkSettings
        from ..models.octo_print_server import OctoPrintServer
        from ..models.pi_mdns_urls import PiMdnsUrls
        from ..models.pi_nats_app import PiNatsApp
        from ..models.pi_shortname_urls import PiShortnameUrls
        from ..models.pi_urls import PiUrls
        from ..models.system_info import SystemInfo
        from ..models.user import User
        from ..models.webrtc_stream import WebrtcStream

        d = src_dict.copy()
        id = d.pop("id")

        network_settings = NetworkSettings.from_dict(d.pop("network_settings"))

        user = User.from_dict(d.pop("user"))

        system_info = SystemInfo.from_dict(d.pop("system_info"))

        webrtc_edge = WebrtcStream.from_dict(d.pop("webrtc_edge"))

        webrtc_cloud = WebrtcStream.from_dict(d.pop("webrtc_cloud"))

        octoprint_server = OctoPrintServer.from_dict(d.pop("octoprint_server"))

        nats_app = PiNatsApp.from_dict(d.pop("nats_app"))

        urls = PiUrls.from_dict(d.pop("urls"))

        shortname_urls = PiShortnameUrls.from_dict(d.pop("shortname_urls"))

        mdns_urls = PiMdnsUrls.from_dict(d.pop("mdns_urls"))

        created_dt = isoparse(d.pop("created_dt"))

        last_boot = d.pop("last_boot")

        _sbc = d.pop("sbc", UNSET)
        sbc: Union[Unset, SbcEnum]
        if isinstance(_sbc, Unset):
            sbc = UNSET
        else:
            sbc = SbcEnum(_sbc)

        hostname = d.pop("hostname", UNSET)

        favorite = d.pop("favorite", UNSET)

        setup_finished = d.pop("setup_finished", UNSET)

        pi = cls(
            id=id,
            network_settings=network_settings,
            user=user,
            system_info=system_info,
            webrtc_edge=webrtc_edge,
            webrtc_cloud=webrtc_cloud,
            octoprint_server=octoprint_server,
            nats_app=nats_app,
            urls=urls,
            shortname_urls=shortname_urls,
            mdns_urls=mdns_urls,
            created_dt=created_dt,
            last_boot=last_boot,
            sbc=sbc,
            hostname=hostname,
            favorite=favorite,
            setup_finished=setup_finished,
        )

        pi.additional_properties = d
        return pi

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
