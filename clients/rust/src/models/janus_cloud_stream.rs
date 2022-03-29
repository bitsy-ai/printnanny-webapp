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
pub struct JanusCloudStream {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "auth")]
    pub auth: Option<Box<crate::models::JanusAuth>>,
    #[serde(rename = "api_domain")]
    pub api_domain: String,
    #[serde(rename = "api_port")]
    pub api_port: i32,
    #[serde(rename = "api_url")]
    pub api_url: String,
    #[serde(rename = "admin_url")]
    pub admin_url: String,
    #[serde(rename = "admin_port")]
    pub admin_port: i32,
    #[serde(rename = "rtp_domain")]
    pub rtp_domain: String,
    #[serde(rename = "websocket_url")]
    pub websocket_url: String,
    #[serde(rename = "websocket_port")]
    pub websocket_port: i32,
    #[serde(rename = "config_type")]
    pub config_type: String,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "updated_dt")]
    pub updated_dt: String,
    #[serde(rename = "active", skip_serializing_if = "Option::is_none")]
    pub active: Option<bool>,
    #[serde(rename = "secret", skip_serializing_if = "Option::is_none")]
    pub secret: Option<String>,
    #[serde(rename = "pin", skip_serializing_if = "Option::is_none")]
    pub pin: Option<String>,
    #[serde(rename = "info", skip_serializing_if = "Option::is_none")]
    pub info: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "rtp_port", skip_serializing_if = "Option::is_none")]
    pub rtp_port: Option<i32>,
    #[serde(rename = "device")]
    pub device: i32,
}

impl JanusCloudStream {
    pub fn new(id: i32, auth: Option<crate::models::JanusAuth>, api_domain: String, api_port: i32, api_url: String, admin_url: String, admin_port: i32, rtp_domain: String, websocket_url: String, websocket_port: i32, config_type: String, created_dt: String, updated_dt: String, device: i32) -> JanusCloudStream {
        JanusCloudStream {
            id,
            auth: auth.map(Box::new),
            api_domain,
            api_port,
            api_url,
            admin_url,
            admin_port,
            rtp_domain,
            websocket_url,
            websocket_port,
            config_type,
            created_dt,
            updated_dt,
            active: None,
            secret: None,
            pin: None,
            info: None,
            rtp_port: None,
            device,
        }
    }
}


