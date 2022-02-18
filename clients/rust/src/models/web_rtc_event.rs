/*
 * printnanny-api-client
 *
 * Official API client library for print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@print-nanny.com
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct WebRtcEvent {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "event_type")]
    pub event_type: crate::models::WebRtcEventEventTypeEnum,
    #[serde(rename = "deleted")]
    pub deleted: String,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "source")]
    pub source: crate::models::EventSource,
    #[serde(rename = "data", skip_serializing_if = "Option::is_none")]
    pub data: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "polymorphic_ctype")]
    pub polymorphic_ctype: i32,
    #[serde(rename = "user")]
    pub user: i32,
    #[serde(rename = "device")]
    pub device: i32,
    #[serde(rename = "stream", skip_serializing_if = "Option::is_none")]
    pub stream: Option<i32>,
}

impl WebRtcEvent {
    pub fn new(id: i32, event_type: crate::models::WebRtcEventEventTypeEnum, deleted: String, created_dt: String, source: crate::models::EventSource, polymorphic_ctype: i32, user: i32, device: i32) -> WebRtcEvent {
        WebRtcEvent {
            id,
            event_type,
            deleted,
            created_dt,
            source,
            data: None,
            polymorphic_ctype,
            user,
            device,
            stream: None,
        }
    }
}


