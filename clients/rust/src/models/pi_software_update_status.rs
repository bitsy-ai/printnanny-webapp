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
pub struct PiSoftwareUpdateStatus {
    #[serde(rename = "id")]
    pub id: String,
    #[serde(rename = "subject_pattern")]
    pub subject_pattern: crate::models::PiSoftwareUpdateStatusSubjectPatternEnum,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
    pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "version")]
    pub version: String,
    #[serde(rename = "event_type")]
    pub event_type: crate::models::PiSoftwareUpdateStatusType,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl PiSoftwareUpdateStatus {
    pub fn new(id: String, subject_pattern: crate::models::PiSoftwareUpdateStatusSubjectPatternEnum, created_dt: String, version: String, event_type: crate::models::PiSoftwareUpdateStatusType, pi: i32) -> PiSoftwareUpdateStatus {
        PiSoftwareUpdateStatus {
            id,
            subject_pattern,
            created_dt,
            payload: None,
            version,
            event_type,
            pi,
        }
    }
}


