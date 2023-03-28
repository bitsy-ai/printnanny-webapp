/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.131.5
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct VideoRecording {
    #[serde(rename = "id", skip_serializing_if = "Option::is_none")]
    pub id: Option<String>,
    #[serde(rename = "mp4_upload_url")]
    pub mp4_upload_url: String,
    #[serde(rename = "mp4_size")]
    pub mp4_size: Option<i32>,
    #[serde(rename = "cloud_sync_done", skip_serializing_if = "Option::is_none")]
    pub cloud_sync_done: Option<bool>,
    #[serde(rename = "finalize_start", skip_serializing_if = "Option::is_none")]
    pub finalize_start: Option<String>,
    #[serde(rename = "finalize_end", skip_serializing_if = "Option::is_none")]
    pub finalize_end: Option<String>,
    #[serde(rename = "finalize_task_id")]
    pub finalize_task_id: Option<String>,
    #[serde(rename = "recording_start", skip_serializing_if = "Option::is_none")]
    pub recording_start: Option<String>,
    #[serde(rename = "recording_end", skip_serializing_if = "Option::is_none")]
    pub recording_end: Option<String>,
    #[serde(rename = "gcode_file_name", skip_serializing_if = "Option::is_none")]
    pub gcode_file_name: Option<String>,
    #[serde(rename = "mp4_file")]
    pub mp4_file: Option<String>,
    #[serde(rename = "user")]
    pub user: i32,
}

impl VideoRecording {
    pub fn new(mp4_upload_url: String, mp4_size: Option<i32>, finalize_task_id: Option<String>, mp4_file: Option<String>, user: i32) -> VideoRecording {
        VideoRecording {
            id: None,
            mp4_upload_url,
            mp4_size,
            cloud_sync_done: None,
            finalize_start: None,
            finalize_end: None,
            finalize_task_id,
            recording_start: None,
            recording_end: None,
            gcode_file_name: None,
            mp4_file,
            user,
        }
    }
}


