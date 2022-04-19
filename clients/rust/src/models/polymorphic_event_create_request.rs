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
pub struct OctoPrintEventRequest {
        #[serde(rename = "source")]
        pub source: crate::models::EventSource,
        #[serde(rename = "event_name")]
        pub event_name: crate::models::OctoPrintEventName,
        #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
        pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "octoprint_install")]
        pub octoprint_install: i32,
        #[serde(rename = "device")]
        pub device: i32,
}
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct TestEventRequest {
        #[serde(rename = "source")]
        pub source: crate::models::EventSource,
        #[serde(rename = "event_name")]
        pub event_name: crate::models::TestEventName,
        #[serde(rename = "device")]
        pub device: i32,
}
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct WebRtcCommandCreateRequest {
        #[serde(rename = "source")]
        pub source: crate::models::EventSource,
        #[serde(rename = "event_name")]
        pub event_name: crate::models::WebRtcCommandName,
        #[serde(rename = "data", skip_serializing_if = "Option::is_none")]
        pub data: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "device")]
        pub device: i32,
        #[serde(rename = "stream")]
        pub stream: i32,
}
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct WebRtcEventRequest {
        #[serde(rename = "source")]
        pub source: crate::models::EventSource,
        #[serde(rename = "event_name")]
        pub event_name: crate::models::WebRtcEventName,
        #[serde(rename = "data", skip_serializing_if = "Option::is_none")]
        pub data: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "device")]
        pub device: i32,
        #[serde(rename = "stream")]
        pub stream: i32,
}

#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
#[serde(tag = "model")]
pub enum PolymorphicEventCreateRequest {
    #[serde(rename="OctoPrintEvent")]
    OctoPrintEventRequest(OctoPrintEventRequest),
    #[serde(rename="TestEvent")]
    TestEventRequest(TestEventRequest),
    #[serde(rename="WebRTCCommand")]
    WebRtcCommandCreateRequest(WebRtcCommandCreateRequest),
    #[serde(rename="WebRTCEvent")]
    WebRtcEventRequest(WebRtcEventRequest),
}



