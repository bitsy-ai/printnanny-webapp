/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.107.3
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PiNatsApp {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "app_name", skip_serializing_if = "Option::is_none")]
    pub app_name: Option<String>,
    /// Output of `nsc describe account`
    #[serde(rename = "json", skip_serializing_if = "Option::is_none")]
    pub json: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "pi")]
    pub pi: i32,
    #[serde(rename = "organization")]
    pub organization: Box<crate::models::NatsOrganization>,
    #[serde(rename = "organization_user")]
    pub organization_user: i32,
    #[serde(rename = "nats_server_uri")]
    pub nats_server_uri: String,
    #[serde(rename = "nats_ws_uri")]
    pub nats_ws_uri: String,
    #[serde(rename = "nats_subject_pattern")]
    pub nats_subject_pattern: String,
    #[serde(rename = "nats_subject_pattern_template")]
    pub nats_subject_pattern_template: String,
}

impl PiNatsApp {
    pub fn new(id: i32, pi: i32, organization: crate::models::NatsOrganization, organization_user: i32, nats_server_uri: String, nats_ws_uri: String, nats_subject_pattern: String, nats_subject_pattern_template: String) -> PiNatsApp {
        PiNatsApp {
            id,
            app_name: None,
            json: None,
            pi,
            organization: Box::new(organization),
            organization_user,
            nats_server_uri,
            nats_ws_uri,
            nats_subject_pattern,
            nats_subject_pattern_template,
        }
    }
}


