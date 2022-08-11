/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.100.7
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PiBootStatusRequest {
    #[serde(rename = "subject_pattern")]
    pub subject_pattern: crate::models::PiBootStatusSubjectPatternEnum,
    #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
    pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "event_type")]
    pub event_type: crate::models::PiBootStatusType,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl PiBootStatusRequest {
    pub fn new(subject_pattern: crate::models::PiBootStatusSubjectPatternEnum, event_type: crate::models::PiBootStatusType, pi: i32) -> PiBootStatusRequest {
        PiBootStatusRequest {
            subject_pattern,
            payload: None,
            event_type,
            pi,
        }
    }
}


