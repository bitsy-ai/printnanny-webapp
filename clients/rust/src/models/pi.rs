/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.117.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct Pi {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "last_boot")]
    pub last_boot: Option<String>,
    #[serde(rename = "settings")]
    pub settings: Option<Box<crate::models::PiSettings>>,
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
    #[serde(rename = "urls")]
    pub urls: Box<crate::models::PiUrls>,
    #[serde(rename = "nats_app")]
    pub nats_app: Option<Box<crate::models::PiNatsApp>>,
    #[serde(rename = "sbc", skip_serializing_if = "Option::is_none")]
    pub sbc: Option<crate::models::SbcEnum>,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    /// Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension)
    #[serde(rename = "hostname", skip_serializing_if = "Option::is_none")]
    pub hostname: Option<String>,
    #[serde(rename = "fqdn", skip_serializing_if = "Option::is_none")]
    pub fqdn: Option<String>,
    #[serde(rename = "favorite", skip_serializing_if = "Option::is_none")]
    pub favorite: Option<bool>,
    #[serde(rename = "setup_finished", skip_serializing_if = "Option::is_none")]
    pub setup_finished: Option<bool>,
}

impl Pi {
    pub fn new(id: i32, last_boot: Option<String>, settings: Option<crate::models::PiSettings>, user: Option<crate::models::User>, system_info: Option<crate::models::SystemInfo>, webrtc_edge: Option<crate::models::WebrtcStream>, webrtc_cloud: Option<crate::models::WebrtcStream>, octoprint_server: Option<crate::models::OctoPrintServer>, urls: crate::models::PiUrls, nats_app: Option<crate::models::PiNatsApp>, created_dt: String) -> Pi {
        Pi {
            id,
            last_boot,
            settings: settings.map(Box::new),
            user: user.map(Box::new),
            system_info: system_info.map(Box::new),
            webrtc_edge: webrtc_edge.map(Box::new),
            webrtc_cloud: webrtc_cloud.map(Box::new),
            octoprint_server: octoprint_server.map(Box::new),
            urls: Box::new(urls),
            nats_app: nats_app.map(Box::new),
            sbc: None,
            created_dt,
            hostname: None,
            fqdn: None,
            favorite: None,
            setup_finished: None,
        }
    }
}


