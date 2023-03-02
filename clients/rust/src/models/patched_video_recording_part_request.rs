/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.127.3
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PatchedVideoRecordingPartRequest {
    #[serde(rename = "id", skip_serializing_if = "Option::is_none")]
    pub id: Option<String>,
    #[serde(rename = "part", skip_serializing_if = "Option::is_none")]
    pub part: Option<i32>,
    #[serde(rename = "size", skip_serializing_if = "Option::is_none")]
    pub size: Option<i64>,
    #[serde(rename = "sync_start", skip_serializing_if = "Option::is_none")]
    pub sync_start: Option<String>,
    #[serde(rename = "sync_end", skip_serializing_if = "Option::is_none")]
    pub sync_end: Option<String>,
    #[serde(rename = "video_recording", skip_serializing_if = "Option::is_none")]
    pub video_recording: Option<String>,
}

impl PatchedVideoRecordingPartRequest {
    pub fn new() -> PatchedVideoRecordingPartRequest {
        PatchedVideoRecordingPartRequest {
            id: None,
            part: None,
            size: None,
            sync_start: None,
            sync_end: None,
            video_recording: None,
        }
    }
}

