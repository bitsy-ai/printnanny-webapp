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
pub struct PrintSessionRequest {
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "octoprint_device")]
    pub octoprint_device: i32,
    #[serde(rename = "active", skip_serializing_if = "Option::is_none")]
    pub active: Option<bool>,
    #[serde(rename = "session")]
    pub session: String,
    #[serde(rename = "filepos", skip_serializing_if = "Option::is_none")]
    pub filepos: Option<i32>,
    #[serde(rename = "print_progress", skip_serializing_if = "Option::is_none")]
    pub print_progress: Option<i32>,
    #[serde(rename = "time_elapsed", skip_serializing_if = "Option::is_none")]
    pub time_elapsed: Option<i32>,
    #[serde(rename = "time_remaining", skip_serializing_if = "Option::is_none")]
    pub time_remaining: Option<i32>,
    #[serde(rename = "printer_profile", skip_serializing_if = "Option::is_none")]
    pub printer_profile: Option<i32>,
    #[serde(rename = "gcode_file", skip_serializing_if = "Option::is_none")]
    pub gcode_file: Option<i32>,
    #[serde(rename = "gcode_filename", skip_serializing_if = "Option::is_none")]
    pub gcode_filename: Option<String>,
    #[serde(rename = "octoprint_job", skip_serializing_if = "Option::is_none")]
    pub octoprint_job: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "print_job_status", skip_serializing_if = "Option::is_none")]
    pub print_job_status: Option<Box<crate::models::OctoJobEvent>>,
}

impl PrintSessionRequest {
    pub fn new(created_dt: String, octoprint_device: i32, session: String) -> PrintSessionRequest {
        PrintSessionRequest {
            created_dt,
            octoprint_device,
            active: None,
            session,
            filepos: None,
            print_progress: None,
            time_elapsed: None,
            time_remaining: None,
            printer_profile: None,
            gcode_file: None,
            gcode_filename: None,
            octoprint_job: None,
            print_job_status: None,
        }
    }
}


