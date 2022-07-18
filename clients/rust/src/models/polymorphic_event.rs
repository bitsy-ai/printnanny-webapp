/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct OctoPrintEvent {
        #[serde(rename = "id")]
        pub id: i32,
        #[serde(rename = "created_dt")]
        pub created_dt: String,
        #[serde(rename = "source")]
        pub source: crate::models::EventSource,
        #[serde(rename = "event_name")]
        pub event_name: crate::models::OctoPrintEventName,
        #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
        pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "polymorphic_ctype")]
        pub polymorphic_ctype: i32,
        #[serde(rename = "user")]
        pub user: i32,
        #[serde(rename = "octoprint_server")]
        pub octoprint_server: i32,
        #[serde(rename = "device")]
        pub device: i32,
}
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct TestEvent {
        #[serde(rename = "id")]
        pub id: i32,
        #[serde(rename = "created_dt")]
        pub created_dt: String,
        #[serde(rename = "source")]
        pub source: crate::models::EventSource,
        #[serde(rename = "event_name")]
        pub event_name: crate::models::TestEventName,
        #[serde(rename = "polymorphic_ctype")]
        pub polymorphic_ctype: i32,
        #[serde(rename = "user")]
        pub user: i32,
        #[serde(rename = "device")]
        pub device: i32,
}
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct WebRtcCommand {
        #[serde(rename = "id")]
        pub id: i32,
        #[serde(rename = "stream")]
        pub stream: Option<Box<crate::models::JanusStream>>,
        #[serde(rename = "created_dt")]
        pub created_dt: String,
        #[serde(rename = "source")]
        pub source: crate::models::EventSource,
        #[serde(rename = "event_name")]
        pub event_name: crate::models::WebRtcCommandName,
        #[serde(rename = "data", skip_serializing_if = "Option::is_none")]
        pub data: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "polymorphic_ctype")]
        pub polymorphic_ctype: i32,
        #[serde(rename = "user")]
        pub user: i32,
        #[serde(rename = "device")]
        pub device: i32,
}
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct WebRtcEvent {
        #[serde(rename = "id")]
        pub id: i32,
        #[serde(rename = "created_dt")]
        pub created_dt: String,
        #[serde(rename = "source")]
        pub source: crate::models::EventSource,
        #[serde(rename = "event_name")]
        pub event_name: crate::models::WebRtcEventName,
        #[serde(rename = "data", skip_serializing_if = "Option::is_none")]
        pub data: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "polymorphic_ctype")]
        pub polymorphic_ctype: i32,
        #[serde(rename = "user")]
        pub user: i32,
        #[serde(rename = "device")]
        pub device: i32,
        #[serde(rename = "stream")]
        pub stream: i32,
}

#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
#[serde(tag = "model")]
pub enum PolymorphicEvent {
    #[serde(rename="OctoPrintEvent")]
    OctoPrintEvent(OctoPrintEvent),
    #[serde(rename="TestEvent")]
    TestEvent(TestEvent),
    #[serde(rename="WebRTCCommand")]
    WebRtcCommand(WebRtcCommand),
    #[serde(rename="WebRTCEvent")]
    WebRtcEvent(WebRtcEvent),
}




