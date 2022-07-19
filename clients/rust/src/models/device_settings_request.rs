/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.95.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct DeviceSettingsRequest {
    /// Send camera stream to PrintNanny Cloud
    #[serde(rename = "cloud_video_enabled", skip_serializing_if = "Option::is_none")]
    pub cloud_video_enabled: Option<bool>,
    /// Send telemetry and performance profiling data to PrintNanny Cloud
    #[serde(rename = "telemetry_enabled", skip_serializing_if = "Option::is_none")]
    pub telemetry_enabled: Option<bool>,
    #[serde(rename = "device")]
    pub device: i32,
}

impl DeviceSettingsRequest {
    pub fn new(device: i32) -> DeviceSettingsRequest {
        DeviceSettingsRequest {
            cloud_video_enabled: None,
            telemetry_enabled: None,
            device,
        }
    }
}


