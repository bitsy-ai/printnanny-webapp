/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct ApplianceRequest {
    #[serde(rename = "pki")]
    pub pki: Box<crate::models::AppliancePkiRequest>,
    #[serde(rename = "ansible_facts")]
    pub ansible_facts: Box<crate::models::AnsibleFactsRequest>,
    #[serde(rename = "hostname")]
    pub hostname: String,
    #[serde(rename = "user")]
    pub user: i32,
}

impl ApplianceRequest {
    pub fn new(pki: crate::models::AppliancePkiRequest, ansible_facts: crate::models::AnsibleFactsRequest, hostname: String, user: i32) -> ApplianceRequest {
        ApplianceRequest {
            pki: Box::new(pki),
            ansible_facts: Box::new(ansible_facts),
            hostname,
            user,
        }
    }
}


