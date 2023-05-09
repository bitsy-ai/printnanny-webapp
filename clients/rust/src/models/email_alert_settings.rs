/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.134.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct EmailAlertSettings {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "updated_dt")]
    pub updated_dt: String,
    #[serde(rename = "progress_percent", skip_serializing_if = "Option::is_none")]
    pub progress_percent: Option<i32>,
    #[serde(rename = "enabled", skip_serializing_if = "Option::is_none")]
    pub enabled: Option<bool>,
    #[serde(rename = "event_types", skip_serializing_if = "Option::is_none")]
    pub event_types: Option<Vec<crate::models::EventTypesEnum>>,
    #[serde(rename = "user")]
    pub user: i32,
}

impl EmailAlertSettings {
    pub fn new(id: i32, created_dt: String, updated_dt: String, user: i32) -> EmailAlertSettings {
        EmailAlertSettings {
            id,
            created_dt,
            updated_dt,
            progress_percent: None,
            enabled: None,
            event_types: None,
            user,
        }
    }
}


