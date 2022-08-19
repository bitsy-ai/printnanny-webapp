/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.102.3
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PiBootCommandRequest {
    #[serde(rename = "subject_pattern")]
    pub subject_pattern: crate::models::PiBootCommandSubjectPatternEnum,
    #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
    pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "event_type")]
    pub event_type: crate::models::PiBootCommandType,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl PiBootCommandRequest {
    pub fn new(subject_pattern: crate::models::PiBootCommandSubjectPatternEnum, event_type: crate::models::PiBootCommandType, pi: i32) -> PiBootCommandRequest {
        PiBootCommandRequest {
            subject_pattern,
            payload: None,
            event_type,
            pi,
        }
    }
}


