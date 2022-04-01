/*
 * printnanny-api-client
 *
 * Official API client library forprintnanny.ai print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PatchedJanusEdgeStreamRequest {
    #[serde(rename = "auth", skip_serializing_if = "Option::is_none")]
    pub auth: Option<Box<crate::models::JanusAuthRequest>>,
    #[serde(rename = "api_domain", skip_serializing_if = "Option::is_none")]
    pub api_domain: Option<String>,
    #[serde(rename = "api_port", skip_serializing_if = "Option::is_none")]
    pub api_port: Option<i32>,
    #[serde(rename = "admin_port", skip_serializing_if = "Option::is_none")]
    pub admin_port: Option<i32>,
    #[serde(rename = "rtp_domain", skip_serializing_if = "Option::is_none")]
    pub rtp_domain: Option<String>,
    #[serde(rename = "websocket_port", skip_serializing_if = "Option::is_none")]
    pub websocket_port: Option<i32>,
    #[serde(rename = "active", skip_serializing_if = "Option::is_none")]
    pub active: Option<bool>,
    #[serde(rename = "secret", skip_serializing_if = "Option::is_none")]
    pub secret: Option<String>,
    #[serde(rename = "pin", skip_serializing_if = "Option::is_none")]
    pub pin: Option<String>,
    #[serde(rename = "info", skip_serializing_if = "Option::is_none")]
    pub info: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "ws_port", skip_serializing_if = "Option::is_none")]
    pub ws_port: Option<i32>,
    #[serde(rename = "rtp_port", skip_serializing_if = "Option::is_none")]
    pub rtp_port: Option<i32>,
    #[serde(rename = "device", skip_serializing_if = "Option::is_none")]
    pub device: Option<i32>,
}

impl PatchedJanusEdgeStreamRequest {
    pub fn new() -> PatchedJanusEdgeStreamRequest {
        PatchedJanusEdgeStreamRequest {
            auth: None,
            api_domain: None,
            api_port: None,
            admin_port: None,
            rtp_domain: None,
            websocket_port: None,
            active: None,
            secret: None,
            pin: None,
            info: None,
            ws_port: None,
            rtp_port: None,
            device: None,
        }
    }
}


