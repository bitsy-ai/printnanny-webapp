/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.118.4
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PiCamCommand {
    #[serde(rename = "id", skip_serializing_if = "Option::is_none")]
    pub id: Option<String>,
    #[serde(rename = "created_dt", skip_serializing_if = "Option::is_none")]
    pub created_dt: Option<String>,
    #[serde(rename = "subject_pattern")]
    pub subject_pattern: crate::models::PiCamCommandSubjectPatternEnum,
    #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
    pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "event_type")]
    pub event_type: crate::models::PiCamCommandType,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl PiCamCommand {
    pub fn new(subject_pattern: crate::models::PiCamCommandSubjectPatternEnum, event_type: crate::models::PiCamCommandType, pi: i32) -> PiCamCommand {
        PiCamCommand {
            id: None,
            created_dt: None,
            subject_pattern,
            payload: None,
            event_type,
            pi,
        }
    }
}


