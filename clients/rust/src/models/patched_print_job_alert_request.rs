/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.132.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PatchedPrintJobAlertRequest {
    #[serde(rename = "event_type", skip_serializing_if = "Option::is_none")]
    pub event_type: Option<crate::models::EventTypeEnum>,
    #[serde(rename = "event_source", skip_serializing_if = "Option::is_none")]
    pub event_source: Option<crate::models::EventSourceEnum>,
    #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
    pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "pi", skip_serializing_if = "Option::is_none")]
    pub pi: Option<i32>,
}

impl PatchedPrintJobAlertRequest {
    pub fn new() -> PatchedPrintJobAlertRequest {
        PatchedPrintJobAlertRequest {
            event_type: None,
            event_source: None,
            payload: None,
            pi: None,
        }
    }
}


