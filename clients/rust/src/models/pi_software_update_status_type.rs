/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.100.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum PiSoftwareUpdateStatusType {
    #[serde(rename = "SwupdateStarted")]
    SwupdateStarted,
    #[serde(rename = "SwupdateSuccess")]
    SwupdateSuccess,
    #[serde(rename = "SwupdateError")]
    SwupdateError,

}

impl ToString for PiSoftwareUpdateStatusType {
    fn to_string(&self) -> String {
        match self {
            Self::SwupdateStarted => String::from("SwupdateStarted"),
            Self::SwupdateSuccess => String::from("SwupdateSuccess"),
            Self::SwupdateError => String::from("SwupdateError"),
        }
    }
}

impl Default for PiSoftwareUpdateStatusType {
    fn default() -> PiSoftwareUpdateStatusType {
        Self::SwupdateStarted
    }
}



