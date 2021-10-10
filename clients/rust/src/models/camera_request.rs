/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct CameraRequest {
    #[serde(rename = "name")]
    pub name: String,
    #[serde(rename = "camera_type")]
    pub camera_type: crate::models::CameraTypeEnum,
    #[serde(rename = "camera_source")]
    pub camera_source: String,
    #[serde(rename = "camera_source_type")]
    pub camera_source_type: crate::models::CameraSourceTypeEnum,
    #[serde(rename = "user")]
    pub user: i32,
    #[serde(rename = "appliance")]
    pub appliance: i32,
}

impl CameraRequest {
    pub fn new(name: String, camera_type: crate::models::CameraTypeEnum, camera_source: String, camera_source_type: crate::models::CameraSourceTypeEnum, user: i32, appliance: i32) -> CameraRequest {
        CameraRequest {
            name,
            camera_type,
            camera_source,
            camera_source_type,
            user,
            appliance,
        }
    }
}


