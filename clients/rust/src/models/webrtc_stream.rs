/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.124.4
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct WebrtcStream {
    #[serde(rename = "active", skip_serializing_if = "Option::is_none")]
    pub active: Option<bool>,
    #[serde(rename = "admin_port")]
    pub admin_port: i32,
    #[serde(rename = "admin_secret")]
    pub admin_secret: String,
    #[serde(rename = "admin_url")]
    pub admin_url: String,
    #[serde(rename = "api_domain")]
    pub api_domain: String,
    #[serde(rename = "api_port")]
    pub api_port: i32,
    #[serde(rename = "api_token")]
    pub api_token: String,
    #[serde(rename = "api_url")]
    pub api_url: String,
    #[serde(rename = "config_type", skip_serializing_if = "Option::is_none")]
    pub config_type: Option<crate::models::JanusConfigType>,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "info")]
    pub info: ::std::collections::HashMap<String, serde_json::Value>,
    #[serde(rename = "is_admin")]
    pub is_admin: bool,
    #[serde(rename = "pi")]
    pub pi: i32,
    #[serde(rename = "pt")]
    pub pt: i32,
    #[serde(rename = "rtp_domain")]
    pub rtp_domain: String,
    #[serde(rename = "video_rtp_port")]
    pub video_rtp_port: Option<i32>,
    #[serde(rename = "data_rtp_port")]
    pub data_rtp_port: Option<i32>,
    #[serde(rename = "rtpmap")]
    pub rtpmap: String,
    #[serde(rename = "stream_pin")]
    pub stream_pin: String,
    #[serde(rename = "stream_secret")]
    pub stream_secret: String,
    #[serde(rename = "updated_dt")]
    pub updated_dt: String,
    #[serde(rename = "ws_port")]
    pub ws_port: i32,
    #[serde(rename = "ws_url")]
    pub ws_url: String,
}

impl WebrtcStream {
    pub fn new(admin_port: i32, admin_secret: String, admin_url: String, api_domain: String, api_port: i32, api_token: String, api_url: String, created_dt: String, id: i32, info: ::std::collections::HashMap<String, serde_json::Value>, is_admin: bool, pi: i32, pt: i32, rtp_domain: String, video_rtp_port: Option<i32>, data_rtp_port: Option<i32>, rtpmap: String, stream_pin: String, stream_secret: String, updated_dt: String, ws_port: i32, ws_url: String) -> WebrtcStream {
        WebrtcStream {
            active: None,
            admin_port,
            admin_secret,
            admin_url,
            api_domain,
            api_port,
            api_token,
            api_url,
            config_type: None,
            created_dt,
            id,
            info,
            is_admin,
            pi,
            pt,
            rtp_domain,
            video_rtp_port,
            data_rtp_port,
            rtpmap,
            stream_pin,
            stream_secret,
            updated_dt,
            ws_port,
            ws_url,
        }
    }
}


