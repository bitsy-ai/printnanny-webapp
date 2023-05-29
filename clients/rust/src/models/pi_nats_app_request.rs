/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.135.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PiNatsAppRequest {
    #[serde(rename = "app_name", skip_serializing_if = "Option::is_none")]
    pub app_name: Option<String>,
    /// Output of `nsc describe account`
    #[serde(rename = "json", skip_serializing_if = "Option::is_none")]
    pub json: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "pi")]
    pub pi: i32,
    #[serde(rename = "organization")]
    pub organization: Box<crate::models::NatsOrganizationRequest>,
    #[serde(rename = "organization_user")]
    pub organization_user: i32,
}

impl PiNatsAppRequest {
    pub fn new(pi: i32, organization: crate::models::NatsOrganizationRequest, organization_user: i32) -> PiNatsAppRequest {
        PiNatsAppRequest {
            app_name: None,
            json: None,
            pi,
            organization: Box::new(organization),
            organization_user,
        }
    }
}


