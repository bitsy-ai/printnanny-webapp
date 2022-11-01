/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.111.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OctoPrintClientStatusRequest {
    #[serde(rename = "subject_pattern")]
    pub subject_pattern: crate::models::OctoPrintClientStatusSubjectPatternEnum,
    #[serde(rename = "payload")]
    pub payload: Box<crate::models::OctoPrintClientStatusPayloadRequest>,
    #[serde(rename = "event_type")]
    pub event_type: crate::models::OctoPrintClientStatusType,
    #[serde(rename = "octoprint_server")]
    pub octoprint_server: i32,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl OctoPrintClientStatusRequest {
    pub fn new(subject_pattern: crate::models::OctoPrintClientStatusSubjectPatternEnum, payload: crate::models::OctoPrintClientStatusPayloadRequest, event_type: crate::models::OctoPrintClientStatusType, octoprint_server: i32, pi: i32) -> OctoPrintClientStatusRequest {
        OctoPrintClientStatusRequest {
            subject_pattern,
            payload: Box::new(payload),
            event_type,
            octoprint_server,
            pi,
        }
    }
}


