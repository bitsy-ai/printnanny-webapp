/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.128.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct VideoRecordingPartRequest {
    #[serde(rename = "id")]
    pub id: String,
    #[serde(rename = "size")]
    pub size: i64,
    #[serde(rename = "buffer_index")]
    pub buffer_index: i64,
    #[serde(rename = "buffer_runningtime")]
    pub buffer_runningtime: i64,
    #[serde(rename = "file_name")]
    pub file_name: String,
    #[serde(rename = "sync_start", skip_serializing_if = "Option::is_none")]
    pub sync_start: Option<String>,
    #[serde(rename = "sync_end", skip_serializing_if = "Option::is_none")]
    pub sync_end: Option<String>,
    #[serde(rename = "video_recording")]
    pub video_recording: String,
}

impl VideoRecordingPartRequest {
    pub fn new(id: String, size: i64, buffer_index: i64, buffer_runningtime: i64, file_name: String, video_recording: String) -> VideoRecordingPartRequest {
        VideoRecordingPartRequest {
            id,
            size,
            buffer_index,
            buffer_runningtime,
            file_name,
            sync_start: None,
            sync_end: None,
            video_recording,
        }
    }
}


