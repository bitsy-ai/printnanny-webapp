/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.124.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct WebrtcStreamRequest {
    #[serde(rename = "active", skip_serializing_if = "Option::is_none")]
    pub active: Option<bool>,
    #[serde(rename = "config_type", skip_serializing_if = "Option::is_none")]
    pub config_type: Option<crate::models::JanusConfigType>,
}

impl WebrtcStreamRequest {
    pub fn new() -> WebrtcStreamRequest {
        WebrtcStreamRequest {
            active: None,
            config_type: None,
        }
    }
}


