/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.131.7
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct VideoRecordingPart {
    #[serde(rename = "id")]
    pub id: String,
    #[serde(rename = "deleted_by_cascade")]
    pub deleted_by_cascade: bool,
    #[serde(rename = "size")]
    pub size: i64,
    #[serde(rename = "buffer_index")]
    pub buffer_index: i64,
    #[serde(rename = "buffer_runningtime")]
    pub buffer_runningtime: i64,
    #[serde(rename = "file_name")]
    pub file_name: String,
    #[serde(rename = "mp4_file")]
    pub mp4_file: String,
    #[serde(rename = "sync_start")]
    pub sync_start: String,
    #[serde(rename = "sync_end")]
    pub sync_end: String,
    #[serde(rename = "video_recording")]
    pub video_recording: String,
    #[serde(rename = "user")]
    pub user: i32,
}

impl VideoRecordingPart {
    pub fn new(id: String, deleted_by_cascade: bool, size: i64, buffer_index: i64, buffer_runningtime: i64, file_name: String, mp4_file: String, sync_start: String, sync_end: String, video_recording: String, user: i32) -> VideoRecordingPart {
        VideoRecordingPart {
            id,
            deleted_by_cascade,
            size,
            buffer_index,
            buffer_runningtime,
            file_name,
            mp4_file,
            sync_start,
            sync_end,
            video_recording,
            user,
        }
    }
}


