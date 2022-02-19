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
pub struct WebRtcEvent {
        #[serde(rename = "id")]
        id: i32,
        #[serde(rename = "deleted")]
        deleted: String,
        #[serde(rename = "created_dt")]
        created_dt: String,
        #[serde(rename = "source")]
        source: crate::models::EventSource,
        #[serde(rename = "event_type")]
        event_type: crate::models::WebRtcEventType,
        #[serde(rename = "data", skip_serializing_if = "Option::is_none")]
        data: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "polymorphic_ctype")]
        polymorphic_ctype: i32,
        #[serde(rename = "user")]
        user: i32,
        #[serde(rename = "device")]
        device: i32,
        #[serde(rename = "stream", skip_serializing_if = "Option::is_none")]
        stream: Option<i32>,
}

#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
#[serde(tag = "event_type")]
pub enum PolymorphicEvent {
    #[serde(rename="WebRTCEvent")]
    WebRtcEvent(WebRtcEvent),
}




