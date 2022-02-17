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
pub struct PatchedJanusStreamRequest {
    #[serde(rename = "config_type", skip_serializing_if = "Option::is_none")]
    pub config_type: Option<crate::models::JanusConfigType>,
    #[serde(rename = "active", skip_serializing_if = "Option::is_none")]
    pub active: Option<bool>,
    #[serde(rename = "secret", skip_serializing_if = "Option::is_none")]
    pub secret: Option<String>,
    #[serde(rename = "pin", skip_serializing_if = "Option::is_none")]
    pub pin: Option<String>,
    #[serde(rename = "info", skip_serializing_if = "Option::is_none")]
    pub info: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "device", skip_serializing_if = "Option::is_none")]
    pub device: Option<i32>,
}

impl PatchedJanusStreamRequest {
    pub fn new() -> PatchedJanusStreamRequest {
        PatchedJanusStreamRequest {
            config_type: None,
            active: None,
            secret: None,
            pin: None,
            info: None,
            device: None,
        }
    }
}


