/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.102.3
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OctoPrintSettings {
    #[serde(rename = "id")]
    pub id: i32,
    /// Start OctoPrint service
    #[serde(rename = "octoprint_enabled", skip_serializing_if = "Option::is_none")]
    pub octoprint_enabled: Option<bool>,
    /// Send OctoPrint events related to print job status/progress to PrintNanny Cloud https://docs.octoprint.org/en/master/events/index.html
    #[serde(rename = "events_enabled", skip_serializing_if = "Option::is_none")]
    pub events_enabled: Option<bool>,
    /// Sync Gcode files to/from PrintNanny Cloud
    #[serde(rename = "sync_gcode", skip_serializing_if = "Option::is_none")]
    pub sync_gcode: Option<bool>,
    /// Sync Printer Profiles to/from PrintNanny Cloud
    #[serde(rename = "sync_printer_profiles", skip_serializing_if = "Option::is_none")]
    pub sync_printer_profiles: Option<bool>,
    /// Upload OctoPrint backups to PrintNanny Cloud
    #[serde(rename = "sync_backups", skip_serializing_if = "Option::is_none")]
    pub sync_backups: Option<bool>,
    #[serde(rename = "auto_backup", skip_serializing_if = "Option::is_none")]
    pub auto_backup: Option<String>,
    #[serde(rename = "updated_dt")]
    pub updated_dt: String,
    #[serde(rename = "octoprint_server")]
    pub octoprint_server: i32,
}

impl OctoPrintSettings {
    pub fn new(id: i32, updated_dt: String, octoprint_server: i32) -> OctoPrintSettings {
        OctoPrintSettings {
            id,
            octoprint_enabled: None,
            events_enabled: None,
            sync_gcode: None,
            sync_printer_profiles: None,
            sync_backups: None,
            auto_backup: None,
            updated_dt,
            octoprint_server,
        }
    }
}


