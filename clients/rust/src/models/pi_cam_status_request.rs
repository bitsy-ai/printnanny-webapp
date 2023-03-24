/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.129.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PiCamStatusRequest {
    #[serde(rename = "id", skip_serializing_if = "Option::is_none")]
    pub id: Option<String>,
    #[serde(rename = "created_dt", skip_serializing_if = "Option::is_none")]
    pub created_dt: Option<String>,
    #[serde(rename = "subject_pattern")]
    pub subject_pattern: crate::models::PiCamStatusSubjectPatternEnum,
    #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
    pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "event_type")]
    pub event_type: crate::models::PiCamStatusType,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl PiCamStatusRequest {
    pub fn new(subject_pattern: crate::models::PiCamStatusSubjectPatternEnum, event_type: crate::models::PiCamStatusType, pi: i32) -> PiCamStatusRequest {
        PiCamStatusRequest {
            id: None,
            created_dt: None,
            subject_pattern,
            payload: None,
            event_type,
            pi,
        }
    }
}


