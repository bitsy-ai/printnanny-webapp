/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.119.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum PiCamCommandType {
    #[serde(rename = "CamStart")]
    CamStart,
    #[serde(rename = "CamStop")]
    CamStop,

}

impl ToString for PiCamCommandType {
    fn to_string(&self) -> String {
        match self {
            Self::CamStart => String::from("CamStart"),
            Self::CamStop => String::from("CamStop"),
        }
    }
}

impl Default for PiCamCommandType {
    fn default() -> PiCamCommandType {
        Self::CamStart
    }
}




