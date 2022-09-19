/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.108.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OctoPrintClientStatus {
    #[serde(rename = "id")]
    pub id: String,
    #[serde(rename = "subject_pattern")]
    pub subject_pattern: crate::models::OctoPrintClientStatusSubjectPatternEnum,
    #[serde(rename = "payload")]
    pub payload: Box<crate::models::OctoPrintClientStatusPayload>,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "event_type")]
    pub event_type: crate::models::OctoPrintClientStatusType,
    #[serde(rename = "octoprint_server")]
    pub octoprint_server: i32,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl OctoPrintClientStatus {
    pub fn new(id: String, subject_pattern: crate::models::OctoPrintClientStatusSubjectPatternEnum, payload: crate::models::OctoPrintClientStatusPayload, created_dt: String, event_type: crate::models::OctoPrintClientStatusType, octoprint_server: i32, pi: i32) -> OctoPrintClientStatus {
        OctoPrintClientStatus {
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


