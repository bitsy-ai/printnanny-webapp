/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.96.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct Device {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "last_boot")]
    pub last_boot: String,
    #[serde(rename = "alert_settings")]
    pub alert_settings: Option<Box<crate::models::AlertSettings>>,
    #[serde(rename = "settings")]
    pub settings: Option<Box<crate::models::DeviceSettings>>,
    #[serde(rename = "cloudiot_device")]
    pub cloudiot_device: Option<Box<crate::models::CloudiotDevice>>,
    #[serde(rename = "user")]
    pub user: Option<Box<crate::models::User>>,
    #[serde(rename = "system_info")]
    pub system_info: Option<Box<crate::models::SystemInfo>>,
    #[serde(rename = "public_key")]
    pub public_key: Option<Box<crate::models::PublicKey>>,
    #[serde(rename = "webrtc_edge")]
    pub webrtc_edge: Option<Box<crate::models::WebrtcStream>>,
    #[serde(rename = "webrtc_cloud")]
    pub webrtc_cloud: Option<Box<crate::models::WebrtcStream>>,
    #[serde(rename = "octoprint_server")]
    pub octoprint_server: Option<Box<crate::models::OctoPrintServer>>,
    #[serde(rename = "urls")]
    pub urls: Box<crate::models::DeviceUrls>,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    /// Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension)
    #[serde(rename = "hostname", skip_serializing_if = "Option::is_none")]
    pub hostname: Option<String>,
    #[serde(rename = "fqdn", skip_serializing_if = "Option::is_none")]
    pub fqdn: Option<String>,
    #[serde(rename = "favorite", skip_serializing_if = "Option::is_none")]
    pub favorite: Option<bool>,
    #[serde(rename = "ws_connected", skip_serializing_if = "Option::is_none")]
    pub ws_connected: Option<bool>,
}

impl Device {
    pub fn new(id: i32, last_boot: String, alert_settings: Option<crate::models::AlertSettings>, settings: Option<crate::models::DeviceSettings>, cloudiot_device: Option<crate::models::CloudiotDevice>, user: Option<crate::models::User>, system_info: Option<crate::models::SystemInfo>, public_key: Option<crate::models::PublicKey>, webrtc_edge: Option<crate::models::WebrtcStream>, webrtc_cloud: Option<crate::models::WebrtcStream>, octoprint_server: Option<crate::models::OctoPrintServer>, urls: crate::models::DeviceUrls, created_dt: String) -> Device {
        Device {
            id,
            last_boot,
            alert_settings: alert_settings.map(Box::new),
            settings: settings.map(Box::new),
            cloudiot_device: cloudiot_device.map(Box::new),
            user: user.map(Box::new),
            system_info: system_info.map(Box::new),
            public_key: public_key.map(Box::new),
            webrtc_edge: webrtc_edge.map(Box::new),
            webrtc_cloud: webrtc_cloud.map(Box::new),
            octoprint_server: octoprint_server.map(Box::new),
            urls: Box::new(urls),
            created_dt,
            hostname: None,
            fqdn: None,
            favorite: None,
            ws_connected: None,
        }
    }
}


