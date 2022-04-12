/*
 * printnanny-api-client
 *
 * Official API client library forprintnanny.ai print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OctoPrintEventRequest {
    #[serde(rename = "model")]
    pub model: crate::models::OctoPrintEventModelEnum,
    #[serde(rename = "source")]
    pub source: crate::models::EventSource,
    /// Broadcast to events websocket: /ws/events
    #[serde(rename = "send_ws", skip_serializing_if = "Option::is_none")]
    pub send_ws: Option<bool>,
    #[serde(rename = "event_name")]
    pub event_name: crate::models::OctoPrintEventEventNameEnum,
    #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
    pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "octoprint_install")]
    pub octoprint_install: i32,
    #[serde(rename = "device")]
    pub device: i32,
}

impl OctoPrintEventRequest {
    pub fn new(model: crate::models::OctoPrintEventModelEnum, source: crate::models::EventSource, event_name: crate::models::OctoPrintEventEventNameEnum, octoprint_install: i32, device: i32) -> OctoPrintEventRequest {
        OctoPrintEventRequest {
            model,
            source,
            send_ws: None,
            event_name,
            payload: None,
            octoprint_install,
            device,
        }
    }
}


