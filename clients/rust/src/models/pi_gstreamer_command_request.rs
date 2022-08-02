/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.99.3
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PiGstreamerCommandRequest {
    #[serde(rename = "source")]
    pub source: crate::models::SourceEnum,
    #[serde(rename = "subject")]
    pub subject: String,
    #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
    pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "event_type")]
    pub event_type: crate::models::PiGstreamerCommandType,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl PiGstreamerCommandRequest {
    pub fn new(source: crate::models::SourceEnum, subject: String, event_type: crate::models::PiGstreamerCommandType, pi: i32) -> PiGstreamerCommandRequest {
        PiGstreamerCommandRequest {
            source,
            subject,
            payload: None,
            event_type,
            pi,
        }
    }
}


