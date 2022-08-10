/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.100.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum PiSoftwareUpdateStatusModelEnum {
    #[serde(rename = "PiSoftwareUpdateStatus")]
    PiSoftwareUpdateStatus,

}

impl ToString for PiSoftwareUpdateStatusModelEnum {
    fn to_string(&self) -> String {
        match self {
            Self::PiSoftwareUpdateStatus => String::from("PiSoftwareUpdateStatus"),
        }
    }
}

impl Default for PiSoftwareUpdateStatusModelEnum {
    fn default() -> PiSoftwareUpdateStatusModelEnum {
        Self::PiSoftwareUpdateStatus
    }
}




