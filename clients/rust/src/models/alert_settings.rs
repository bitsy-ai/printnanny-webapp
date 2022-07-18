/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct AlertSettings {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "updated_dt")]
    pub updated_dt: String,
    #[serde(rename = "alert_methods", skip_serializing_if = "Option::is_none")]
    pub alert_methods: Option<Vec<crate::models::AlertMethodsEnum>>,
    #[serde(rename = "event_types", skip_serializing_if = "Option::is_none")]
    pub event_types: Option<Vec<crate::models::EventTypesEnum>>,
    /// Send notifications to a Discord channel. Please check out this guide to <a href='https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks'>generate a webhook</a> url and paste it here.
    #[serde(rename = "discord_webhook", skip_serializing_if = "Option::is_none")]
    pub discord_webhook: Option<String>,
    /// Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress
    #[serde(rename = "print_progress_percent", skip_serializing_if = "Option::is_none")]
    pub print_progress_percent: Option<i32>,
    #[serde(rename = "user")]
    pub user: i32,
}

impl AlertSettings {
    pub fn new(id: i32, created_dt: String, updated_dt: String, user: i32) -> AlertSettings {
        AlertSettings {
            id,
            created_dt,
            updated_dt,
            alert_methods: None,
            event_types: None,
            discord_webhook: None,
            print_progress_percent: None,
            user,
        }
    }
}


