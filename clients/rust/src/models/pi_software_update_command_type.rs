/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.121.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum PiSoftwareUpdateCommandType {
    #[serde(rename = "Swupdate")]
    Swupdate,
    #[serde(rename = "SwupdateRollback")]
    SwupdateRollback,

}

impl ToString for PiSoftwareUpdateCommandType {
    fn to_string(&self) -> String {
        match self {
            Self::Swupdate => String::from("Swupdate"),
            Self::SwupdateRollback => String::from("SwupdateRollback"),
        }
    }
}

impl Default for PiSoftwareUpdateCommandType {
    fn default() -> PiSoftwareUpdateCommandType {
        Self::Swupdate
    }
}




