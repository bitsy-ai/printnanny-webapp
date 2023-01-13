/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.123.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OctoPrintGcodeEvent {
    #[serde(rename = "id")]
    pub id: String,
    #[serde(rename = "subject_pattern")]
    pub subject_pattern: crate::models::OctoPrintGcodeEventSubjectPatternEnum,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
    pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "event_type")]
    pub event_type: crate::models::GcodeEventType,
    #[serde(rename = "octoprint_server")]
    pub octoprint_server: i32,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl OctoPrintGcodeEvent {
    pub fn new(id: String, subject_pattern: crate::models::OctoPrintGcodeEventSubjectPatternEnum, created_dt: String, event_type: crate::models::GcodeEventType, octoprint_server: i32, pi: i32) -> OctoPrintGcodeEvent {
        OctoPrintGcodeEvent {
            id,
            subject_pattern,
            created_dt,
            payload: None,
            event_type,
            octoprint_server,
            pi,
        }
    }
}


