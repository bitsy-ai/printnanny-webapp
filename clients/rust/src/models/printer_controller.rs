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
pub struct PrinterController {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "software", skip_serializing_if = "Option::is_none")]
    pub software: Option<Box<crate::models::SoftwareEnum>>,
    #[serde(rename = "deleted")]
    pub deleted: String,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "updated_dt")]
    pub updated_dt: String,
    #[serde(rename = "polymorphic_ctype")]
    pub polymorphic_ctype: i32,
    #[serde(rename = "user")]
    pub user: i32,
    #[serde(rename = "device")]
    pub device: i32,
}

impl PrinterController {
    pub fn new(id: i32, deleted: String, created_dt: String, updated_dt: String, polymorphic_ctype: i32, user: i32, device: i32) -> PrinterController {
        PrinterController {
            id,
            software: None,
            deleted,
            created_dt,
            updated_dt,
            polymorphic_ctype,
            user,
            device,
        }
    }
}


