/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.125.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum RecordingStatusEnum {
    #[serde(rename = "pending")]
    Pending,
    #[serde(rename = "inprogress")]
    Inprogress,
    #[serde(rename = "done")]
    Done,

}

impl ToString for RecordingStatusEnum {
    fn to_string(&self) -> String {
        match self {
            Self::Pending => String::from("pending"),
            Self::Inprogress => String::from("inprogress"),
            Self::Done => String::from("done"),
        }
    }
}

impl Default for RecordingStatusEnum {
    fn default() -> RecordingStatusEnum {
        Self::Pending
    }
}




