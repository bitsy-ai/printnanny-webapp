/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.96.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OctoPrintEvent {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "model")]
    pub model: crate::models::OctoPrintEventModel,
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

impl OctoPrintEvent {
    pub fn new(id: i32, model: crate::models::OctoPrintEventModel, created_dt: String, source: crate::models::EventSource, event_name: crate::models::OctoPrintEventName, polymorphic_ctype: i32, user: i32, octoprint_server: i32, device: i32) -> OctoPrintEvent {
        OctoPrintEvent {
            id,
            model,
            created_dt,
            source,
            event_name,
            payload: None,
            polymorphic_ctype,
            user,
            octoprint_server,
            device,
        }
    }
}


