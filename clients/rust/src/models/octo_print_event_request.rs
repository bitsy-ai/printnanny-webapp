/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.94.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OctoPrintEventRequest {
    #[serde(rename = "model")]
    pub model: crate::models::OctoPrintEventModel,
    #[serde(rename = "source")]
    pub source: crate::models::EventSource,
    #[serde(rename = "event_name")]
    pub event_name: crate::models::OctoPrintEventName,
    #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
    pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "octoprint_server")]
    pub octoprint_server: i32,
    #[serde(rename = "device")]
    pub device: i32,
}

impl OctoPrintEventRequest {
    pub fn new(model: crate::models::OctoPrintEventModel, source: crate::models::EventSource, event_name: crate::models::OctoPrintEventName, octoprint_server: i32, device: i32) -> OctoPrintEventRequest {
        OctoPrintEventRequest {
            model,
            source,
            event_name,
            payload: None,
            octoprint_server,
            device,
        }
    }
}


