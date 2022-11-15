/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.117.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OctoPrintPrinterStatus {
    #[serde(rename = "id")]
    pub id: String,
    #[serde(rename = "subject_pattern")]
    pub subject_pattern: crate::models::OctoPrintPrinterStatusSubjectPatternEnum,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
    pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "event_type")]
    pub event_type: crate::models::OctoPrintPrinterStatusType,
    #[serde(rename = "octoprint_server")]
    pub octoprint_server: i32,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl OctoPrintPrinterStatus {
    pub fn new(id: String, subject_pattern: crate::models::OctoPrintPrinterStatusSubjectPatternEnum, created_dt: String, event_type: crate::models::OctoPrintPrinterStatusType, octoprint_server: i32, pi: i32) -> OctoPrintPrinterStatus {
        OctoPrintPrinterStatus {
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


