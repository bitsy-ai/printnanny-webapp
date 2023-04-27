/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.133.4
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PrintJobAlertRequest {
    #[serde(rename = "event_type")]
    pub event_type: crate::models::EventTypeEnum,
    #[serde(rename = "event_source")]
    pub event_source: crate::models::EventSourceEnum,
    #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
    pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl PrintJobAlertRequest {
    pub fn new(event_type: crate::models::EventTypeEnum, event_source: crate::models::EventSourceEnum, pi: i32) -> PrintJobAlertRequest {
        PrintJobAlertRequest {
            event_type,
            event_source,
            payload: None,
            pi,
        }
    }
}


