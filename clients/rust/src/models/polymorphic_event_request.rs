/*
 * printnanny-api-client
 *
 * Official API client library for print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@print-nanny.com
 * Generated by: https://openapi-generator.tech
 */



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
}

#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
#[serde(tag = "event_type")]
pub enum PolymorphicEventRequest {
    #[serde(rename="WebRTCEvent")]
    WebRtcEventRequest(WebRtcEventRequest),
}




