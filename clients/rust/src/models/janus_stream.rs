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
pub struct JanusStream {
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "updated_dt")]
    pub updated_dt: String,
    #[serde(rename = "config_type")]
    pub config_type: Option<Box<crate::models::JanusConfigType>>,
    #[serde(rename = "active", skip_serializing_if = "Option::is_none")]
    pub active: Option<bool>,
    #[serde(rename = "device")]
    pub device: i32,
    #[serde(rename = "stream_secret", skip_serializing_if = "Option::is_none")]
    pub stream_secret: Option<String>,
    #[serde(rename = "stream_pin", skip_serializing_if = "Option::is_none")]
    pub stream_pin: Option<String>,
    #[serde(rename = "api_token", skip_serializing_if = "Option::is_none")]
    pub api_token: Option<String>,
    #[serde(rename = "admin_secret")]
    pub admin_secret: String,
    #[serde(rename = "rtp_port", skip_serializing_if = "Option::is_none")]
    pub rtp_port: Option<i32>,
    #[serde(rename = "rtp_domain")]
    pub rtp_domain: String,
    #[serde(rename = "pt")]
    pub pt: i32,
    #[serde(rename = "rtpmap")]
    pub rtpmap: String,
    #[serde(rename = "admin_port")]
    pub admin_port: i32,
    #[serde(rename = "admin_url")]
    pub admin_url: String,
    #[serde(rename = "api_port")]
    pub api_port: i32,
    #[serde(rename = "api_url")]
    pub api_url: String,
    #[serde(rename = "api_domain")]
    pub api_domain: String,
    #[serde(rename = "ws_port")]
    pub ws_port: i32,
    #[serde(rename = "ws_url")]
    pub ws_url: String,
}

impl JanusStream {
    pub fn new(created_dt: String, updated_dt: String, config_type: Option<crate::models::JanusConfigType>, device: i32, admin_secret: String, rtp_domain: String, pt: i32, rtpmap: String, admin_port: i32, admin_url: String, api_port: i32, api_url: String, api_domain: String, ws_port: i32, ws_url: String) -> JanusStream {
        JanusStream {
            created_dt,
            updated_dt,
            config_type: config_type.map(Box::new),
            active: None,
            device,
            stream_secret: None,
            stream_pin: None,
            api_token: None,
            admin_secret,
            rtp_port: None,
            rtp_domain,
            pt,
            rtpmap,
            admin_port,
            admin_url,
            api_port,
            api_url,
            api_domain,
            ws_port,
            ws_url,
        }
    }
}


