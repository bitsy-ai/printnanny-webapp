/*
 * printnanny-api-client
 *
 * Official API client library forprintnanny.ai print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PatchedDeviceRequest {
    #[serde(rename = "monitoring_active", skip_serializing_if = "Option::is_none")]
    pub monitoring_active: Option<bool>,
    #[serde(rename = "setup_complete", skip_serializing_if = "Option::is_none")]
    pub setup_complete: Option<bool>,
    #[serde(rename = "release_channel", skip_serializing_if = "Option::is_none")]
    pub release_channel: Option<Box<crate::models::DeviceReleaseChannel>>,
    /// Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension)
    #[serde(rename = "hostname", skip_serializing_if = "Option::is_none")]
    pub hostname: Option<String>,
    #[serde(rename = "edition", skip_serializing_if = "Option::is_none")]
    pub edition: Option<crate::models::OsEdition>,
}

impl PatchedDeviceRequest {
    pub fn new() -> PatchedDeviceRequest {
        PatchedDeviceRequest {
            monitoring_active: None,
            setup_complete: None,
            release_channel: None,
            hostname: None,
            edition: None,
        }
    }
}


