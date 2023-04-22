/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.133.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct VideoRecordingFinalizeRequest {
    #[serde(rename = "recording_end")]
    pub recording_end: String,
}

impl VideoRecordingFinalizeRequest {
    pub fn new(recording_end: String) -> VideoRecordingFinalizeRequest {
        VideoRecordingFinalizeRequest {
            recording_end,
        }
    }
}


