/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.100.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum PiGstreamerEventEventTypeEnum {
    #[serde(rename = "StartCommand")]
    StartCommand,
    #[serde(rename = "StartSuccess")]
    StartSuccess,
    #[serde(rename = "StartError")]
    StartError,
    #[serde(rename = "StopCommand")]
    StopCommand,
    #[serde(rename = "StopSuccess")]
    StopSuccess,
    #[serde(rename = "StopError")]
    StopError,

}

impl ToString for PiGstreamerEventEventTypeEnum {
    fn to_string(&self) -> String {
        match self {
            Self::StartCommand => String::from("StartCommand"),
            Self::StartSuccess => String::from("StartSuccess"),
            Self::StartError => String::from("StartError"),
            Self::StopCommand => String::from("StopCommand"),
            Self::StopSuccess => String::from("StopSuccess"),
            Self::StopError => String::from("StopError"),
        }
    }
}

impl Default for PiGstreamerEventEventTypeEnum {
    fn default() -> PiGstreamerEventEventTypeEnum {
        Self::StartCommand
    }
}




