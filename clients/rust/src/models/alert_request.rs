/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.97.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct AlertRequest {
    #[serde(rename = "octoprint_device", skip_serializing_if = "Option::is_none")]
    pub octoprint_device: Option<i32>,
    #[serde(rename = "event_type", skip_serializing_if = "Option::is_none")]
    pub event_type: Option<Box<crate::models::EventTypeEnum>>,
    #[serde(rename = "seen", skip_serializing_if = "Option::is_none")]
    pub seen: Option<bool>,
    #[serde(rename = "sent", skip_serializing_if = "Option::is_none")]
    pub sent: Option<bool>,
}

impl AlertRequest {
    pub fn new() -> AlertRequest {
        AlertRequest {
            octoprint_device: None,
            event_type: None,
            seen: None,
            sent: None,
        }
    }
}


