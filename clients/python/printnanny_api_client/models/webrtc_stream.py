import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.janus_config_type import JanusConfigType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webrtc_stream_info import WebrtcStreamInfo


T = TypeVar("T", bound="WebrtcStream")


@attr.s(auto_attribs=True)
class WebrtcStream:
    """
    Attributes:
        admin_port (int):
        admin_secret (str):
        admin_url (str):
        api_domain (str):
        api_port (int):
        api_token (str):
        api_url (str):
        created_dt (datetime.datetime):
        id (int):
        info (WebrtcStreamInfo):
        is_admin (bool):
        pi (int):
        pt (int):
        rtp_domain (str):
        rtpmap (str):
        stream_pin (str):
        stream_secret (str):
        updated_dt (datetime.datetime):
        ws_port (int):
        ws_url (str):
        active (Union[Unset, bool]):
        config_type (Union[Unset, JanusConfigType]):
        video_rtp_port (Optional[int]):
        data_rtp_port (Optional[int]):
    """

    admin_port: int
    admin_secret: str
    admin_url: str
    api_domain: str
    api_port: int
    api_token: str
    api_url: str
    created_dt: datetime.datetime
    id: int
    info: "WebrtcStreamInfo"
    is_admin: bool
    pi: int
    pt: int
    rtp_domain: str
    rtpmap: str
    stream_pin: str
    stream_secret: str
    updated_dt: datetime.datetime
    ws_port: int
    ws_url: str
    video_rtp_port: Optional[int]
    data_rtp_port: Optional[int]
    active: Union[Unset, bool] = UNSET
    config_type: Union[Unset, JanusConfigType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        admin_port = self.admin_port
        admin_secret = self.admin_secret
        admin_url = self.admin_url
        api_domain = self.api_domain
        api_port = self.api_port
        api_token = self.api_token
        api_url = self.api_url
        created_dt = self.created_dt.isoformat()

        id = self.id
        info = self.info.to_dict()

        is_admin = self.is_admin
        pi = self.pi
        pt = self.pt
        rtp_domain = self.rtp_domain
        rtpmap = self.rtpmap
        stream_pin = self.stream_pin
        stream_secret = self.stream_secret
        updated_dt = self.updated_dt.isoformat()

        ws_port = self.ws_port
        ws_url = self.ws_url
        active = self.active
        config_type: Union[Unset, str] = UNSET
        if not isinstance(self.config_type, Unset):
            config_type = self.config_type.value

        video_rtp_port = self.video_rtp_port
        data_rtp_port = self.data_rtp_port

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "admin_port": admin_port,
                "admin_secret": admin_secret,
                "admin_url": admin_url,
                "api_domain": api_domain,
                "api_port": api_port,
                "api_token": api_token,
                "api_url": api_url,
                "created_dt": created_dt,
                "id": id,
                "info": info,
                "is_admin": is_admin,
                "pi": pi,
                "pt": pt,
                "rtp_domain": rtp_domain,
                "rtpmap": rtpmap,
                "stream_pin": stream_pin,
                "stream_secret": stream_secret,
                "updated_dt": updated_dt,
                "ws_port": ws_port,
                "ws_url": ws_url,
                "video_rtp_port": video_rtp_port,
                "data_rtp_port": data_rtp_port,
            }
        )
        if active is not UNSET:
            field_dict["active"] = active
        if config_type is not UNSET:
            field_dict["config_type"] = config_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.webrtc_stream_info import WebrtcStreamInfo

        d = src_dict.copy()
        admin_port = d.pop("admin_port")

        admin_secret = d.pop("admin_secret")

        admin_url = d.pop("admin_url")

        api_domain = d.pop("api_domain")

        api_port = d.pop("api_port")

        api_token = d.pop("api_token")

        api_url = d.pop("api_url")

        created_dt = isoparse(d.pop("created_dt"))

        id = d.pop("id")

        info = WebrtcStreamInfo.from_dict(d.pop("info"))

        is_admin = d.pop("is_admin")

        pi = d.pop("pi")

        pt = d.pop("pt")

        rtp_domain = d.pop("rtp_domain")

        rtpmap = d.pop("rtpmap")

        stream_pin = d.pop("stream_pin")

        stream_secret = d.pop("stream_secret")

        updated_dt = isoparse(d.pop("updated_dt"))

        ws_port = d.pop("ws_port")

        ws_url = d.pop("ws_url")

        active = d.pop("active", UNSET)

        _config_type = d.pop("config_type", UNSET)
        config_type: Union[Unset, JanusConfigType]
        if isinstance(_config_type, Unset):
            config_type = UNSET
        else:
            config_type = JanusConfigType(_config_type)

        video_rtp_port = d.pop("video_rtp_port")

        data_rtp_port = d.pop("data_rtp_port")

        webrtc_stream = cls(
            admin_port=admin_port,
            admin_secret=admin_secret,
            admin_url=admin_url,
            api_domain=api_domain,
            api_port=api_port,
            api_token=api_token,
            api_url=api_url,
            created_dt=created_dt,
            id=id,
            info=info,
            is_admin=is_admin,
            pi=pi,
            pt=pt,
            rtp_domain=rtp_domain,
            rtpmap=rtpmap,
            stream_pin=stream_pin,
            stream_secret=stream_secret,
            updated_dt=updated_dt,
            ws_port=ws_port,
            ws_url=ws_url,
            active=active,
            config_type=config_type,
            video_rtp_port=video_rtp_port,
            data_rtp_port=data_rtp_port,
        )

        webrtc_stream.additional_properties = d
        return webrtc_stream

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
