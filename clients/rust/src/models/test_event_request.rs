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
pub struct TestEventRequest {
    #[serde(rename = "event_type")]
    pub event_type: crate::models::TestEventEventTypeEnum,
    #[serde(rename = "source")]
    pub source: crate::models::EventSource,
    /// Broadcast to events websocket: /ws/events
    #[serde(rename = "send_ws", skip_serializing_if = "Option::is_none")]
    pub send_ws: Option<bool>,
    #[serde(rename = "event_name")]
    pub event_name: crate::models::TestEventName,
    /// Broadcast to mqtt topic: /devices/{device-id}/commands/
    #[serde(rename = "send_mqtt", skip_serializing_if = "Option::is_none")]
    pub send_mqtt: Option<bool>,
    #[serde(rename = "device")]
    pub device: i32,
}

impl TestEventRequest {
    pub fn new(event_type: crate::models::TestEventEventTypeEnum, source: crate::models::EventSource, event_name: crate::models::TestEventName, device: i32) -> TestEventRequest {
        TestEventRequest {
            event_type,
            source,
            send_ws: None,
            event_name,
            send_mqtt: None,
            device,
        }
    }
}


