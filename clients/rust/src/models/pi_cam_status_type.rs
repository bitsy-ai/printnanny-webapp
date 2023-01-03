/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.118.4
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum PiCamStatusType {
    #[serde(rename = "CamStarted")]
    CamStarted,
    #[serde(rename = "CamStartSuccess")]
    CamStartSuccess,
    #[serde(rename = "CamError")]
    CamError,
    #[serde(rename = "CamStopped")]
    CamStopped,

}

impl ToString for PiCamStatusType {
    fn to_string(&self) -> String {
        match self {
            Self::CamStarted => String::from("CamStarted"),
            Self::CamStartSuccess => String::from("CamStartSuccess"),
            Self::CamError => String::from("CamError"),
            Self::CamStopped => String::from("CamStopped"),
        }
    }
}

impl Default for PiCamStatusType {
    fn default() -> PiCamStatusType {
        Self::CamStarted
    }
}




