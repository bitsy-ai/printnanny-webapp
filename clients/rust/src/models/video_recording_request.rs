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
pub struct VideoRecordingRequest {
    #[serde(rename = "id", skip_serializing_if = "Option::is_none")]
    pub id: Option<String>,
    #[serde(rename = "cloud_sync_done", skip_serializing_if = "Option::is_none")]
    pub cloud_sync_done: Option<bool>,
    #[serde(rename = "finalize_start", skip_serializing_if = "Option::is_none")]
    pub finalize_start: Option<String>,
    #[serde(rename = "finalize_end", skip_serializing_if = "Option::is_none")]
    pub finalize_end: Option<String>,
    #[serde(rename = "recording_start", skip_serializing_if = "Option::is_none")]
    pub recording_start: Option<String>,
    #[serde(rename = "recording_end", skip_serializing_if = "Option::is_none")]
    pub recording_end: Option<String>,
    #[serde(rename = "gcode_file_name", skip_serializing_if = "Option::is_none")]
    pub gcode_file_name: Option<String>,
}

impl VideoRecordingRequest {
    pub fn new() -> VideoRecordingRequest {
        VideoRecordingRequest {
            id: None,
            cloud_sync_done: None,
            finalize_start: None,
            finalize_end: None,
            recording_start: None,
            recording_end: None,
            gcode_file_name: None,
        }
    }
}


