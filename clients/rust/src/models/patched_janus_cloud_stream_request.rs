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
pub struct PatchedJanusCloudStreamRequest {
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

impl PatchedJanusCloudStreamRequest {
    pub fn new() -> PatchedJanusCloudStreamRequest {
        PatchedJanusCloudStreamRequest {
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


