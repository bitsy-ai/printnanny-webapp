/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.125.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OctoPrintServerStatus {
    #[serde(rename = "id")]
    pub id: String,
    #[serde(rename = "subject_pattern")]
    pub subject_pattern: crate::models::OctoPrintServerStatusSubjectPatternEnum,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
    pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "event_type")]
    pub event_type: crate::models::OctoPrintServerStatusType,
    #[serde(rename = "octoprint_server")]
    pub octoprint_server: i32,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl OctoPrintServerStatus {
    pub fn new(id: String, subject_pattern: crate::models::OctoPrintServerStatusSubjectPatternEnum, created_dt: String, event_type: crate::models::OctoPrintServerStatusType, octoprint_server: i32, pi: i32) -> OctoPrintServerStatus {
        OctoPrintServerStatus {
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


