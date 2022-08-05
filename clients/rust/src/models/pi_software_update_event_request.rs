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
pub struct PiSoftwareUpdateEventRequest {
    #[serde(rename = "subject")]
    pub subject: String,
    #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
    pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "version")]
    pub version: String,
    #[serde(rename = "event_type")]
    pub event_type: crate::models::PiSoftwareUpdateEventType,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl PiSoftwareUpdateEventRequest {
    pub fn new(subject: String, version: String, event_type: crate::models::PiSoftwareUpdateEventType, pi: i32) -> PiSoftwareUpdateEventRequest {
        PiSoftwareUpdateEventRequest {
            subject,
            payload: None,
            version,
            event_type,
            pi,
        }
    }
}


