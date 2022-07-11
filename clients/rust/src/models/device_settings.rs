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
pub struct DeviceSettings {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "updated_dt")]
    pub updated_dt: String,
    /// Start OctoPrint service
    #[serde(rename = "octoprint_enabled", skip_serializing_if = "Option::is_none")]
    pub octoprint_enabled: Option<bool>,
    /// Send camera stream to PrintNanny Cloud
    #[serde(rename = "cloud_video_enabled", skip_serializing_if = "Option::is_none")]
    pub cloud_video_enabled: Option<bool>,
    /// Send telemetry and performance profiling data to PrintNanny Cloud
    #[serde(rename = "telemetry_enabled", skip_serializing_if = "Option::is_none")]
    pub telemetry_enabled: Option<bool>,
    #[serde(rename = "device")]
    pub device: i32,
}

impl DeviceSettings {
    pub fn new(id: i32, updated_dt: String, device: i32) -> DeviceSettings {
        DeviceSettings {
            id,
            updated_dt,
            octoprint_enabled: None,
            cloud_video_enabled: None,
            telemetry_enabled: None,
            device,
        }
    }
}


