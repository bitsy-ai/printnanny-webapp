/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.125.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct VideoRecordingRequest {
    #[serde(rename = "recording_start", skip_serializing_if = "Option::is_none")]
    pub recording_start: Option<String>,
    #[serde(rename = "recording_end", skip_serializing_if = "Option::is_none")]
    pub recording_end: Option<String>,
    #[serde(rename = "recording_status", skip_serializing_if = "Option::is_none")]
    pub recording_status: Option<crate::models::RecordingStatusEnum>,
    #[serde(rename = "cloud_sync_start", skip_serializing_if = "Option::is_none")]
    pub cloud_sync_start: Option<String>,
    #[serde(rename = "cloud_sync_end", skip_serializing_if = "Option::is_none")]
    pub cloud_sync_end: Option<String>,
    #[serde(rename = "cloud_sync_status", skip_serializing_if = "Option::is_none")]
    pub cloud_sync_status: Option<crate::models::CloudSyncStatusEnum>,
    #[serde(rename = "gcode_file_name", skip_serializing_if = "Option::is_none")]
    pub gcode_file_name: Option<String>,
}

impl VideoRecordingRequest {
    pub fn new() -> VideoRecordingRequest {
        VideoRecordingRequest {
            recording_start: None,
            recording_end: None,
            recording_status: None,
            cloud_sync_start: None,
            cloud_sync_end: None,
            cloud_sync_status: None,
            gcode_file_name: None,
        }
    }
}


