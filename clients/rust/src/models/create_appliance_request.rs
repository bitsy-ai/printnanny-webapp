/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct CreateApplianceRequest {
    #[serde(rename = "ansible_facts")]
    pub ansible_facts: Box<crate::models::CreateAnsibleFactsRequest>,
    #[serde(rename = "hostname")]
    pub hostname: String,
    #[serde(rename = "pki")]
    pub pki: Box<crate::models::CreateAppliancePkiRequest>,
}

impl CreateApplianceRequest {
    pub fn new(ansible_facts: crate::models::CreateAnsibleFactsRequest, hostname: String, pki: crate::models::CreateAppliancePkiRequest) -> CreateApplianceRequest {
        CreateApplianceRequest {
            ansible_facts: Box::new(ansible_facts),
            hostname,
            pki: Box::new(pki),
        }
    }
}


