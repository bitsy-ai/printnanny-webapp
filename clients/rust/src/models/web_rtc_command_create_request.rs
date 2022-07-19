/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.94.3
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct WebRtcCommandCreateRequest {
    #[serde(rename = "model")]
    pub model: crate::models::WebRtcCommandModel,
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

impl WebRtcCommandCreateRequest {
    pub fn new(model: crate::models::WebRtcCommandModel, source: crate::models::EventSource, event_name: crate::models::WebRtcCommandName, device: i32, stream: i32) -> WebRtcCommandCreateRequest {
        WebRtcCommandCreateRequest {
            model,
            source,
            event_name,
            data: None,
            device,
            stream,
        }
    }
}


