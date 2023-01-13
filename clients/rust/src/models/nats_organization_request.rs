/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.124.0
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
    /// Enable JetStream for all users/apps belonging to NatsOrganization account
    #[serde(rename = "jetstream_enabled", skip_serializing_if = "Option::is_none")]
    pub jetstream_enabled: Option<bool>,
    /// JetStream memory resource limits (shared across all users/apps beloning to NatsOrganization account)
    #[serde(rename = "jetstream_max_mem", skip_serializing_if = "Option::is_none")]
    pub jetstream_max_mem: Option<String>,
    /// JetStream file resource limits (shared across all users/apps beloning to NatsOrganization account)
    #[serde(rename = "jetstream_max_file", skip_serializing_if = "Option::is_none")]
    pub jetstream_max_file: Option<String>,
    /// JetStream max number of streams (shared across all users/apps beloning to NatsOrganization account)
    #[serde(rename = "jetstream_max_streams", skip_serializing_if = "Option::is_none")]
    pub jetstream_max_streams: Option<i32>,
    /// JetStream max number of consumers (shared across all users/apps beloning to NatsOrganization account)
    #[serde(rename = "jetstream_max_consumers", skip_serializing_if = "Option::is_none")]
    pub jetstream_max_consumers: Option<i32>,
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
            jetstream_enabled: None,
            jetstream_max_mem: None,
            jetstream_max_file: None,
            jetstream_max_streams: None,
            jetstream_max_consumers: None,
            imports,
            exports,
        }
    }
}


