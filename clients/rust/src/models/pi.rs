/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.131.8
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct Pi {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "last_boot")]
    pub last_boot: Option<String>,
    #[serde(rename = "network_settings")]
    pub network_settings: Option<Box<crate::models::NetworkSettings>>,
    #[serde(rename = "user")]
    pub user: Option<Box<crate::models::User>>,
    #[serde(rename = "system_info")]
    pub system_info: Option<Box<crate::models::SystemInfo>>,
    #[serde(rename = "webrtc_edge")]
    pub webrtc_edge: Option<Box<crate::models::WebrtcStream>>,
    #[serde(rename = "webrtc_cloud")]
    pub webrtc_cloud: Option<Box<crate::models::WebrtcStream>>,
    #[serde(rename = "octoprint_server")]
    pub octoprint_server: Option<Box<crate::models::OctoPrintServer>>,
    #[serde(rename = "hostname")]
    pub hostname: String,
    #[serde(rename = "favorite")]
    pub favorite: bool,
    #[serde(rename = "sbc")]
    pub sbc: crate::models::SbcEnum,
    #[serde(rename = "setup_finished")]
    pub setup_finished: bool,
    #[serde(rename = "nats_app")]
    pub nats_app: Option<Box<crate::models::PiNatsApp>>,
    #[serde(rename = "urls")]
    pub urls: Box<crate::models::PiUrls>,
    #[serde(rename = "shortname_urls")]
    pub shortname_urls: Box<crate::models::PiUrls>,
    #[serde(rename = "mdns_urls")]
    pub mdns_urls: Box<crate::models::PiUrls>,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
}

impl Pi {
    pub fn new(id: i32, last_boot: Option<String>, network_settings: Option<crate::models::NetworkSettings>, user: Option<crate::models::User>, system_info: Option<crate::models::SystemInfo>, webrtc_edge: Option<crate::models::WebrtcStream>, webrtc_cloud: Option<crate::models::WebrtcStream>, octoprint_server: Option<crate::models::OctoPrintServer>, hostname: String, favorite: bool, sbc: crate::models::SbcEnum, setup_finished: bool, nats_app: Option<crate::models::PiNatsApp>, urls: crate::models::PiUrls, shortname_urls: crate::models::PiUrls, mdns_urls: crate::models::PiUrls, created_dt: String) -> Pi {
        Pi {
            id,
            last_boot,
            network_settings: network_settings.map(Box::new),
            user: user.map(Box::new),
            system_info: system_info.map(Box::new),
            webrtc_edge: webrtc_edge.map(Box::new),
            webrtc_cloud: webrtc_cloud.map(Box::new),
            octoprint_server: octoprint_server.map(Box::new),
            hostname,
            favorite,
            sbc,
            setup_finished,
            nats_app: nats_app.map(Box::new),
            urls: Box::new(urls),
            shortname_urls: Box::new(shortname_urls),
            mdns_urls: Box::new(mdns_urls),
            created_dt,
        }
    }
}


