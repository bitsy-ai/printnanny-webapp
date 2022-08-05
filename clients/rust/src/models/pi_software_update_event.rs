/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.100.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PiSoftwareUpdateEvent {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "subject")]
    pub subject: String,
    #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
    pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "version")]
    pub version: String,
    #[serde(rename = "event_type")]
    pub event_type: crate::models::PiSoftwareUpdateEventType,
    #[serde(rename = "polymorphic_ctype")]
    pub polymorphic_ctype: i32,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl PiSoftwareUpdateEvent {
    pub fn new(id: i32, created_dt: String, subject: String, version: String, event_type: crate::models::PiSoftwareUpdateEventType, polymorphic_ctype: i32, pi: i32) -> PiSoftwareUpdateEvent {
        PiSoftwareUpdateEvent {
            id,
            created_dt,
            subject,
            payload: None,
            version,
            event_type,
            polymorphic_ctype,
            pi,
        }
    }
}


