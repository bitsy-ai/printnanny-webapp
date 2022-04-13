/*
 * printnanny-api-client
 *
 * Official API client library forprintnanny.ai print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OctoPrintSettings {
    #[serde(rename = "id")]
    pub id: i32,
    /// Send OctoPrint events to PrintNanny Cloud https://docs.octoprint.org/en/master/events/index.html
    #[serde(rename = "events_enabled", skip_serializing_if = "Option::is_none")]
    pub events_enabled: Option<bool>,
    /// Send telemetry data to PrintNanny Cloud for debugging/analytics purposes
    #[serde(rename = "telemetry_enabled", skip_serializing_if = "Option::is_none")]
    pub telemetry_enabled: Option<bool>,
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
    /// Start PrintNanny monitoring automatically when a print job begins
    #[serde(rename = "monitoring_auto_start", skip_serializing_if = "Option::is_none")]
    pub monitoring_auto_start: Option<bool>,
    /// Pause failing print jobs automatically
    #[serde(rename = "monitoring_auto_pause", skip_serializing_if = "Option::is_none")]
    pub monitoring_auto_pause: Option<bool>,
    #[serde(rename = "octoprint_install")]
    pub octoprint_install: i32,
}

impl OctoPrintSettings {
    pub fn new(id: i32, octoprint_install: i32) -> OctoPrintSettings {
        OctoPrintSettings {
            id,
            events_enabled: None,
            telemetry_enabled: None,
            sync_gcode: None,
            sync_printer_profiles: None,
            sync_backups: None,
            auto_backup: None,
            monitoring_auto_start: None,
            monitoring_auto_pause: None,
            octoprint_install,
        }
    }
}


