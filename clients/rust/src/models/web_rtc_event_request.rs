/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.98.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct WebRtcEventRequest {
    #[serde(rename = "model")]
    pub model: crate::models::WebRtcEventModel,
    #[serde(rename = "source")]
    pub source: crate::models::EventSource,
    #[serde(rename = "event_name")]
    pub event_name: crate::models::WebRtcEventName,
    #[serde(rename = "data", skip_serializing_if = "Option::is_none")]
    pub data: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "pi")]
    pub pi: i32,
    #[serde(rename = "stream")]
    pub stream: i32,
}

impl WebRtcEventRequest {
    pub fn new(model: crate::models::WebRtcEventModel, source: crate::models::EventSource, event_name: crate::models::WebRtcEventName, pi: i32, stream: i32) -> WebRtcEventRequest {
        WebRtcEventRequest {
            model,
            source,
            event_name,
            data: None,
            pi,
            stream,
        }
    }
}


