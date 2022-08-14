/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.101.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PiSoftwareUpdateStatusRequest {
    #[serde(rename = "subject_pattern")]
    pub subject_pattern: crate::models::PiSoftwareUpdateStatusSubjectPatternEnum,
    #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
    pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "version")]
    pub version: String,
    #[serde(rename = "event_type")]
    pub event_type: crate::models::PiSoftwareUpdateStatusType,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl PiSoftwareUpdateStatusRequest {
    pub fn new(subject_pattern: crate::models::PiSoftwareUpdateStatusSubjectPatternEnum, version: String, event_type: crate::models::PiSoftwareUpdateStatusType, pi: i32) -> PiSoftwareUpdateStatusRequest {
        PiSoftwareUpdateStatusRequest {
            subject_pattern,
            payload: None,
            version,
            event_type,
            pi,
        }
    }
}


