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
pub struct PatchedCameraRequest {
    #[serde(rename = "user", skip_serializing_if = "Option::is_none")]
    pub user: Option<i32>,
    #[serde(rename = "device", skip_serializing_if = "Option::is_none")]
    pub device: Option<i32>,
    #[serde(rename = "name", skip_serializing_if = "Option::is_none")]
    pub name: Option<String>,
    #[serde(rename = "camera_type", skip_serializing_if = "Option::is_none")]
    pub camera_type: Option<Box<crate::models::CameraTypeEnum>>,
    #[serde(rename = "camera_source", skip_serializing_if = "Option::is_none")]
    pub camera_source: Option<String>,
}

impl PatchedCameraRequest {
    pub fn new() -> PatchedCameraRequest {
        PatchedCameraRequest {
            user: None,
            device: None,
            name: None,
            camera_type: None,
            camera_source: None,
        }
    }
}


