/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.106.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum TiersModeEnum {
    #[serde(rename = "graduated")]
    Graduated,
    #[serde(rename = "volume")]
    Volume,

}

impl ToString for TiersModeEnum {
    fn to_string(&self) -> String {
        match self {
            Self::Graduated => String::from("graduated"),
            Self::Volume => String::from("volume"),
        }
    }
}

impl Default for TiersModeEnum {
    fn default() -> TiersModeEnum {
        Self::Graduated
    }
}




