/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.99.3
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PiBootEvent {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "source")]
    pub source: crate::models::SourceEnum,
    #[serde(rename = "subject")]
    pub subject: String,
    #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
    pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "event_type")]
    pub event_type: crate::models::PiBootEventType,
    #[serde(rename = "polymorphic_ctype")]
    pub polymorphic_ctype: i32,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl PiBootEvent {
    pub fn new(id: i32, created_dt: String, source: crate::models::SourceEnum, subject: String, event_type: crate::models::PiBootEventType, polymorphic_ctype: i32, pi: i32) -> PiBootEvent {
        PiBootEvent {
            id,
            created_dt,
            source,
            subject,
            payload: None,
            event_type,
            polymorphic_ctype,
            pi,
        }
    }
}


