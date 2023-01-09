/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.120.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OctoPrintGcodeEventRequest {
    #[serde(rename = "subject_pattern")]
    pub subject_pattern: crate::models::OctoPrintGcodeEventSubjectPatternEnum,
    #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
    pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "event_type")]
    pub event_type: crate::models::GcodeEventType,
    #[serde(rename = "octoprint_server")]
    pub octoprint_server: i32,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl OctoPrintGcodeEventRequest {
    pub fn new(subject_pattern: crate::models::OctoPrintGcodeEventSubjectPatternEnum, event_type: crate::models::GcodeEventType, octoprint_server: i32, pi: i32) -> OctoPrintGcodeEventRequest {
        OctoPrintGcodeEventRequest {
            subject_pattern,
            payload: None,
            event_type,
            octoprint_server,
            pi,
        }
    }
}


