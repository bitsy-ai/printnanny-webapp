/*
 * printnanny-api-client
 *
 * Official API client library forprintnanny.ai print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct TestEventRequest {
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
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct WebRtcEventCreateRequest {
        #[serde(rename = "source")]
        pub source: crate::models::EventSource,
        /// Broadcast to events websocket: /ws/events
        #[serde(rename = "send_ws", skip_serializing_if = "Option::is_none")]
        pub send_ws: Option<bool>,
        #[serde(rename = "event_name")]
        pub event_name: crate::models::WebRtcEventName,
        #[serde(rename = "data", skip_serializing_if = "Option::is_none")]
        pub data: Option<::std::collections::HashMap<String, serde_json::Value>>,
        /// Broadcast to mqtt topic: /devices/{device-id}/commands/
        #[serde(rename = "send_mqtt", skip_serializing_if = "Option::is_none")]
        pub send_mqtt: Option<bool>,
        #[serde(rename = "device")]
        pub device: i32,
        #[serde(rename = "stream")]
        pub stream: i32,
}

#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
#[serde(tag = "event_type")]
pub enum PolymorphicEventCreateRequest {
    #[serde(rename="TestEvent")]
    TestEventRequest(TestEventRequest),
    #[serde(rename="WebRTCEvent")]
    WebRtcEventCreateRequest(WebRtcEventCreateRequest),
}



