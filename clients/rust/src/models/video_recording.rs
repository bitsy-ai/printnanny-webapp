/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.122.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct VideoRecording {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "mjr_upload_url")]
    pub mjr_upload_url: String,
    #[serde(rename = "start_dt")]
    pub start_dt: String,
    #[serde(rename = "end_dt", skip_serializing_if = "Option::is_none")]
    pub end_dt: Option<String>,
    #[serde(rename = "name")]
    pub name: String,
    #[serde(rename = "mjr_recording", skip_serializing_if = "Option::is_none")]
    pub mjr_recording: Option<String>,
    #[serde(rename = "user")]
    pub user: i32,
}

impl VideoRecording {
    pub fn new(id: i32, mjr_upload_url: String, start_dt: String, name: String, user: i32) -> VideoRecording {
        VideoRecording {
            id,
            mjr_upload_url,
            start_dt,
            end_dt: None,
            name,
            mjr_recording: None,
            user,
        }
    }
}


