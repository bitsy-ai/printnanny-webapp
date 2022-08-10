/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.100.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct NatsApp {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "app_name", skip_serializing_if = "Option::is_none")]
    pub app_name: Option<String>,
    /// Output of `nsc describe account`
    #[serde(rename = "json")]
    pub json: ::std::collections::HashMap<String, serde_json::Value>,
    #[serde(rename = "pi")]
    pub pi: i32,
    #[serde(rename = "organization")]
    pub organization: i32,
    #[serde(rename = "organization_user")]
    pub organization_user: i32,
    #[serde(rename = "nats_uri")]
    pub nats_uri: String,
}

impl NatsApp {
    pub fn new(id: i32, json: ::std::collections::HashMap<String, serde_json::Value>, pi: i32, organization: i32, organization_user: i32, nats_uri: String) -> NatsApp {
        NatsApp {
            id,
            app_name: None,
            json,
            pi,
            organization,
            organization_user,
            nats_uri,
        }
    }
}

