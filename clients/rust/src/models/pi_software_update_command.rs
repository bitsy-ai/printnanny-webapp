/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.129.5
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PiSoftwareUpdateCommand {
    #[serde(rename = "id", skip_serializing_if = "Option::is_none")]
    pub id: Option<String>,
    #[serde(rename = "created_dt", skip_serializing_if = "Option::is_none")]
    pub created_dt: Option<String>,
    #[serde(rename = "payload")]
    pub payload: Box<crate::models::PiSoftwareUpdatePayload>,
    #[serde(rename = "subject_pattern")]
    pub subject_pattern: crate::models::PiSoftwareUpdateCommandSubjectPatternEnum,
    #[serde(rename = "version")]
    pub version: String,
    #[serde(rename = "event_type")]
    pub event_type: crate::models::PiSoftwareUpdateCommandType,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl PiSoftwareUpdateCommand {
    pub fn new(payload: crate::models::PiSoftwareUpdatePayload, subject_pattern: crate::models::PiSoftwareUpdateCommandSubjectPatternEnum, version: String, event_type: crate::models::PiSoftwareUpdateCommandType, pi: i32) -> PiSoftwareUpdateCommand {
        PiSoftwareUpdateCommand {
            id: None,
            created_dt: None,
            payload: Box::new(payload),
            subject_pattern,
            version,
            event_type,
            pi,
        }
    }
}


