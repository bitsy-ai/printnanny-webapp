/*
 * printnanny-api-client
 *
 * Official API client library for print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@print-nanny.com
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct CameraRequest {
    #[serde(rename = "user")]
    pub user: i32,
    #[serde(rename = "device")]
    pub device: i32,
    #[serde(rename = "name")]
    pub name: String,
    #[serde(rename = "camera_type", skip_serializing_if = "Option::is_none")]
    pub camera_type: Option<Box<crate::models::CameraTypeEnum>>,
    #[serde(rename = "camera_source")]
    pub camera_source: String,
}

impl CameraRequest {
    pub fn new(user: i32, device: i32, name: String, camera_source: String) -> CameraRequest {
        CameraRequest {
            user,
            device,
            name,
            camera_type: None,
            camera_source,
        }
    }
}


