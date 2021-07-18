/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct PrinterProfile {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "deleted")]
    pub deleted: String,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "updated_dt")]
    pub updated_dt: String,
    #[serde(rename = "name")]
    pub name: String,
    #[serde(rename = "local_webcam")]
    pub local_webcam: String,
    #[serde(rename = "polymorphic_ctype")]
    pub polymorphic_ctype: i32,
    #[serde(rename = "user")]
    pub user: i32,
    #[serde(rename = "controller")]
    pub controller: i32,
    #[serde(rename = "device")]
    pub device: i32,
}

impl PrinterProfile {
    pub fn new(id: i32, deleted: String, created_dt: String, updated_dt: String, name: String, local_webcam: String, polymorphic_ctype: i32, user: i32, controller: i32, device: i32) -> PrinterProfile {
        PrinterProfile {
            id,
            deleted,
            created_dt,
            updated_dt,
            name,
            local_webcam,
            polymorphic_ctype,
            user,
            controller,
            device,
        }
    }
}


