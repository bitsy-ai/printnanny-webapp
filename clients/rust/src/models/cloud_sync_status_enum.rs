/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.124.5
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum CloudSyncStatusEnum {
    #[serde(rename = "pending")]
    Pending,
    #[serde(rename = "inprogress")]
    Inprogress,
    #[serde(rename = "done")]
    Done,

}

impl ToString for CloudSyncStatusEnum {
    fn to_string(&self) -> String {
        match self {
            Self::Pending => String::from("pending"),
            Self::Inprogress => String::from("inprogress"),
            Self::Done => String::from("done"),
        }
    }
}

impl Default for CloudSyncStatusEnum {
    fn default() -> CloudSyncStatusEnum {
        Self::Pending
    }
}




