/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PatchedCameraRequest {
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
            name: None,
            camera_type: None,
            camera_source: None,
        }
    }
}


