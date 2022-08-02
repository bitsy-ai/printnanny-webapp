/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.99.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct WebrtcStreamRequest {
    #[serde(rename = "active", skip_serializing_if = "Option::is_none")]
    pub active: Option<bool>,
    #[serde(rename = "stream_secret", skip_serializing_if = "Option::is_none")]
    pub stream_secret: Option<String>,
    #[serde(rename = "stream_pin", skip_serializing_if = "Option::is_none")]
    pub stream_pin: Option<String>,
    #[serde(rename = "api_token", skip_serializing_if = "Option::is_none")]
    pub api_token: Option<String>,
    #[serde(rename = "rtp_port", skip_serializing_if = "Option::is_none")]
    pub rtp_port: Option<i32>,
}

impl WebrtcStreamRequest {
    pub fn new() -> WebrtcStreamRequest {
        WebrtcStreamRequest {
            active: None,
            stream_secret: None,
            stream_pin: None,
            api_token: None,
            rtp_port: None,
        }
    }
}


