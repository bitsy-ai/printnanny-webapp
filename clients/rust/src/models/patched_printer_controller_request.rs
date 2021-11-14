/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PatchedPrinterControllerRequest {
    #[serde(rename = "software", skip_serializing_if = "Option::is_none")]
    pub software: Option<Box<crate::models::SoftwareEnum>>,
    #[serde(rename = "user", skip_serializing_if = "Option::is_none")]
    pub user: Option<i32>,
    #[serde(rename = "device", skip_serializing_if = "Option::is_none")]
    pub device: Option<i32>,
}

impl PatchedPrinterControllerRequest {
    pub fn new() -> PatchedPrinterControllerRequest {
        PatchedPrinterControllerRequest {
            software: None,
            user: None,
            device: None,
        }
    }
}


