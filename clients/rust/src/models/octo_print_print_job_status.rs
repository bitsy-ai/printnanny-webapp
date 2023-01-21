/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.124.7
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OctoPrintPrintJobStatus {
    #[serde(rename = "id")]
    pub id: String,
    #[serde(rename = "subject_pattern")]
    pub subject_pattern: crate::models::OctoPrintPrintJobStatusSubjectPatternEnum,
    #[serde(rename = "payload")]
    pub payload: Box<crate::models::OctoPrintPrintJobPayload>,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "event_type")]
    pub event_type: crate::models::OctoPrintPrintJobStatusType,
    #[serde(rename = "octoprint_server")]
    pub octoprint_server: i32,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl OctoPrintPrintJobStatus {
    pub fn new(id: String, subject_pattern: crate::models::OctoPrintPrintJobStatusSubjectPatternEnum, payload: crate::models::OctoPrintPrintJobPayload, created_dt: String, event_type: crate::models::OctoPrintPrintJobStatusType, octoprint_server: i32, pi: i32) -> OctoPrintPrintJobStatus {
        OctoPrintPrintJobStatus {
            id,
            subject_pattern,
            payload: Box::new(payload),
            created_dt,
            event_type,
            octoprint_server,
            pi,
        }
    }
}


