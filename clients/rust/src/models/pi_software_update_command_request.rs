/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.100.7
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PiSoftwareUpdateCommandRequest {
    #[serde(rename = "payload")]
    pub payload: Box<crate::models::PiSoftwareUpdatePayloadRequest>,
    #[serde(rename = "subject_pattern")]
    pub subject_pattern: crate::models::PiSoftwareUpdateCommandSubjectPatternEnum,
    #[serde(rename = "version")]
    pub version: String,
    #[serde(rename = "event_type")]
    pub event_type: crate::models::PiSoftwareUpdateCommandType,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl PiSoftwareUpdateCommandRequest {
    pub fn new(payload: crate::models::PiSoftwareUpdatePayloadRequest, subject_pattern: crate::models::PiSoftwareUpdateCommandSubjectPatternEnum, version: String, event_type: crate::models::PiSoftwareUpdateCommandType, pi: i32) -> PiSoftwareUpdateCommandRequest {
        PiSoftwareUpdateCommandRequest {
            payload: Box::new(payload),
            subject_pattern,
            version,
            event_type,
            pi,
        }
    }
}


