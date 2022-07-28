/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.98.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct Alert {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "time")]
    pub time: String,
    #[serde(rename = "gcode_file")]
    pub gcode_file: String,
    #[serde(rename = "print_progress")]
    pub print_progress: String,
    #[serde(rename = "time_elapsed")]
    pub time_elapsed: String,
    #[serde(rename = "time_remaining")]
    pub time_remaining: String,
    #[serde(rename = "manage_device_url")]
    pub manage_device_url: Option<String>,
    #[serde(rename = "user")]
    pub user: i32,
    #[serde(rename = "octoprint_device", skip_serializing_if = "Option::is_none")]
    pub octoprint_device: Option<i32>,
    #[serde(rename = "event_type", skip_serializing_if = "Option::is_none")]
    pub event_type: Option<Box<crate::models::EventTypeEnum>>,
    #[serde(rename = "seen", skip_serializing_if = "Option::is_none")]
    pub seen: Option<bool>,
    #[serde(rename = "sent", skip_serializing_if = "Option::is_none")]
    pub sent: Option<bool>,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "updated_dt")]
    pub updated_dt: String,
    #[serde(rename = "message")]
    pub message: String,
}

impl Alert {
    pub fn new(id: i32, time: String, gcode_file: String, print_progress: String, time_elapsed: String, time_remaining: String, manage_device_url: Option<String>, user: i32, created_dt: String, updated_dt: String, message: String) -> Alert {
        Alert {
            id,
            time,
            gcode_file,
            print_progress,
            time_elapsed,
            time_remaining,
            manage_device_url,
            user,
            octoprint_device: None,
            event_type: None,
            seen: None,
            sent: None,
            created_dt,
            updated_dt,
            message,
        }
    }
}


