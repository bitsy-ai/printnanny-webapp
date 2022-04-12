/*
 * printnanny-api-client
 *
 * Official API client library forprintnanny.ai print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum WebRtcEventName {
    #[serde(rename = "stream_start_success")]
    StartSuccess,
    #[serde(rename = "stream_start_error")]
    StartError,
    #[serde(rename = "stream_stop_success")]
    StopSuccess,
    #[serde(rename = "stream_stop_error")]
    StopError,

}

impl ToString for WebRtcEventName {
    fn to_string(&self) -> String {
        match self {
            Self::StartSuccess => String::from("stream_start_success"),
            Self::StartError => String::from("stream_start_error"),
            Self::StopSuccess => String::from("stream_stop_success"),
            Self::StopError => String::from("stream_stop_error"),
        }
    }
}

impl Default for WebRtcEventName {
    fn default() -> WebRtcEventName {
        Self::StartSuccess
    }
}




