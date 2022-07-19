/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.95.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct WebRtcEvent {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "model")]
    pub model: crate::models::WebRtcEventModel,
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

impl WebRtcEvent {
    pub fn new(id: i32, model: crate::models::WebRtcEventModel, created_dt: String, source: crate::models::EventSource, event_name: crate::models::WebRtcEventName, polymorphic_ctype: i32, user: i32, device: i32, stream: i32) -> WebRtcEvent {
        WebRtcEvent {
            id,
            model,
            created_dt,
            source,
            event_name,
            data: None,
            polymorphic_ctype,
            user,
            device,
            stream,
        }
    }
}


