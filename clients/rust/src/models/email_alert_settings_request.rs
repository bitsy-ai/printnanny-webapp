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
pub struct EmailAlertSettingsRequest {
    #[serde(rename = "progress_percent", skip_serializing_if = "Option::is_none")]
    pub progress_percent: Option<i32>,
    #[serde(rename = "enabled", skip_serializing_if = "Option::is_none")]
    pub enabled: Option<bool>,
    #[serde(rename = "event_types", skip_serializing_if = "Option::is_none")]
    pub event_types: Option<Vec<crate::models::EventTypesEnum>>,
}

impl EmailAlertSettingsRequest {
    pub fn new() -> EmailAlertSettingsRequest {
        EmailAlertSettingsRequest {
            progress_percent: None,
            enabled: None,
            event_types: None,
        }
    }
}


