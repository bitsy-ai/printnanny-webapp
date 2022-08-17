/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.102.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PiSoftwareUpdateCommand {
    #[serde(rename = "id")]
    pub id: String,
    #[serde(rename = "payload")]
    pub payload: Box<crate::models::PiSoftwareUpdatePayload>,
    #[serde(rename = "subject_pattern")]
    pub subject_pattern: crate::models::PiSoftwareUpdateCommandSubjectPatternEnum,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "version")]
    pub version: String,
    #[serde(rename = "event_type")]
    pub event_type: crate::models::PiSoftwareUpdateCommandType,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl PiSoftwareUpdateCommand {
    pub fn new(id: String, payload: crate::models::PiSoftwareUpdatePayload, subject_pattern: crate::models::PiSoftwareUpdateCommandSubjectPatternEnum, created_dt: String, version: String, event_type: crate::models::PiSoftwareUpdateCommandType, pi: i32) -> PiSoftwareUpdateCommand {
        PiSoftwareUpdateCommand {
            id,
            payload: Box::new(payload),
            subject_pattern,
            created_dt,
            version,
            event_type,
            pi,
        }
    }
}


