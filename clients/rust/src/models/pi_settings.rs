/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.110.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PiSettings {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "updated_dt")]
    pub updated_dt: String,
    /// Send camera stream to PrintNanny Cloud
    #[serde(rename = "cloud_video_enabled", skip_serializing_if = "Option::is_none")]
    pub cloud_video_enabled: Option<bool>,
    /// Send telemetry and performance profiling data to PrintNanny Cloud
    #[serde(rename = "telemetry_enabled", skip_serializing_if = "Option::is_none")]
    pub telemetry_enabled: Option<bool>,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl PiSettings {
    pub fn new(id: i32, updated_dt: String, pi: i32) -> PiSettings {
        PiSettings {
            id,
            updated_dt,
            cloud_video_enabled: None,
            telemetry_enabled: None,
            pi,
        }
    }
}


