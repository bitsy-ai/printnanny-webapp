/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.121.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OctoPrintPrinterStatusRequest {
    #[serde(rename = "subject_pattern")]
    pub subject_pattern: crate::models::OctoPrintPrinterStatusSubjectPatternEnum,
    #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
    pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "event_type")]
    pub event_type: crate::models::OctoPrintPrinterStatusType,
    #[serde(rename = "octoprint_server")]
    pub octoprint_server: i32,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl OctoPrintPrinterStatusRequest {
    pub fn new(subject_pattern: crate::models::OctoPrintPrinterStatusSubjectPatternEnum, event_type: crate::models::OctoPrintPrinterStatusType, octoprint_server: i32, pi: i32) -> OctoPrintPrinterStatusRequest {
        OctoPrintPrinterStatusRequest {
            subject_pattern,
            payload: None,
            event_type,
            octoprint_server,
            pi,
        }
    }
}


