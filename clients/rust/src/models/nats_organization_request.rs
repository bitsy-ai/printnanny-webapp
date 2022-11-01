/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.112.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct NatsOrganizationRequest {
    /// The name of the organization
    #[serde(rename = "name")]
    pub name: String,
    #[serde(rename = "is_active", skip_serializing_if = "Option::is_none")]
    pub is_active: Option<bool>,
    /// The name in all lowercase, suitable for URL identification
    #[serde(rename = "slug")]
    pub slug: String,
    /// Output of `nsc describe account`
    #[serde(rename = "json", skip_serializing_if = "Option::is_none")]
    pub json: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "imports")]
    pub imports: Vec<i32>,
    #[serde(rename = "exports")]
    pub exports: Vec<i32>,
}

impl NatsOrganizationRequest {
    pub fn new(name: String, slug: String, imports: Vec<i32>, exports: Vec<i32>) -> NatsOrganizationRequest {
        NatsOrganizationRequest {
            name,
            is_active: None,
            slug,
            json: None,
            imports,
            exports,
        }
    }
}


