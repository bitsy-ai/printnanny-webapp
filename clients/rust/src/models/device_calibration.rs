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
pub struct DeviceCalibration {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "updated_dt")]
    pub updated_dt: String,
    #[serde(rename = "octoprint_device")]
    pub octoprint_device: i32,
    #[serde(rename = "fps", skip_serializing_if = "Option::is_none")]
    pub fps: Option<f32>,
    #[serde(rename = "xy", skip_serializing_if = "Option::is_none")]
    pub xy: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "height", skip_serializing_if = "Option::is_none")]
    pub height: Option<i32>,
    #[serde(rename = "width", skip_serializing_if = "Option::is_none")]
    pub width: Option<i32>,
    #[serde(rename = "url")]
    pub url: String,
}

impl DeviceCalibration {
    pub fn new(id: i32, created_dt: String, updated_dt: String, octoprint_device: i32, url: String) -> DeviceCalibration {
        DeviceCalibration {
            id,
            created_dt,
            updated_dt,
            octoprint_device,
            fps: None,
            xy: None,
            height: None,
            width: None,
            url,
        }
    }
}


