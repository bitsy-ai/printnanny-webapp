/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.115.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OctoPrintPrintJobStatusRequest {
    #[serde(rename = "subject_pattern")]
    pub subject_pattern: crate::models::OctoPrintPrintJobStatusSubjectPatternEnum,
    #[serde(rename = "payload")]
    pub payload: Box<crate::models::OctoPrintPrintJobPayloadRequest>,
    #[serde(rename = "event_type")]
    pub event_type: crate::models::OctoPrintPrintJobStatusType,
    #[serde(rename = "octoprint_server")]
    pub octoprint_server: i32,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl OctoPrintPrintJobStatusRequest {
    pub fn new(subject_pattern: crate::models::OctoPrintPrintJobStatusSubjectPatternEnum, payload: crate::models::OctoPrintPrintJobPayloadRequest, event_type: crate::models::OctoPrintPrintJobStatusType, octoprint_server: i32, pi: i32) -> OctoPrintPrintJobStatusRequest {
        OctoPrintPrintJobStatusRequest {
            subject_pattern,
            payload: Box::new(payload),
            event_type,
            octoprint_server,
            pi,
        }
    }
}


