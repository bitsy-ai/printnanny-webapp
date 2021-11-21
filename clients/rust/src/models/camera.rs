/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct Camera {
    #[serde(rename = "id", skip_serializing_if = "Option::is_none")]
    pub id: Option<i32>,
    #[serde(rename = "deleted", skip_serializing_if = "Option::is_none")]
    pub deleted: Option<String>,
    #[serde(rename = "created_dt", skip_serializing_if = "Option::is_none")]
    pub created_dt: Option<String>,
    #[serde(rename = "updated_dt", skip_serializing_if = "Option::is_none")]
    pub updated_dt: Option<String>,
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
    #[serde(rename = "url", skip_serializing_if = "Option::is_none")]
    pub url: Option<String>,
}

impl Camera {
    pub fn new(user: i32, device: i32, name: String, camera_source: String) -> Camera {
        Camera {
            id: None,
            deleted: None,
            created_dt: None,
            updated_dt: None,
            user,
            device,
            name,
            camera_type: None,
            camera_source,
            url: None,
        }
    }
}


