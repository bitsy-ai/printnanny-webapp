/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PrinterController {
    #[serde(rename = "id", skip_serializing_if = "Option::is_none")]
    pub id: Option<i32>,
    #[serde(rename = "user", skip_serializing_if = "Option::is_none")]
    pub user: Option<i32>,
    #[serde(rename = "appliance", skip_serializing_if = "Option::is_none")]
    pub appliance: Option<i32>,
    #[serde(rename = "software", skip_serializing_if = "Option::is_none")]
    pub software: Option<Box<crate::models::SoftwareEnum>>,
    #[serde(rename = "deleted", skip_serializing_if = "Option::is_none")]
    pub deleted: Option<String>,
    #[serde(rename = "created_dt", skip_serializing_if = "Option::is_none")]
    pub created_dt: Option<String>,
    #[serde(rename = "updated_dt", skip_serializing_if = "Option::is_none")]
    pub updated_dt: Option<String>,
    #[serde(rename = "polymorphic_ctype", skip_serializing_if = "Option::is_none")]
    pub polymorphic_ctype: Option<i32>,
}

impl PrinterController {
    pub fn new() -> PrinterController {
        PrinterController {
            id: None,
            user: None,
            appliance: None,
            software: None,
            deleted: None,
            created_dt: None,
            updated_dt: None,
            polymorphic_ctype: None,
        }
    }
}


