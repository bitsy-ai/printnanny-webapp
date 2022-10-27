/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.110.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum StripePriceTiersMode {
    #[serde(rename = "graduated")]
    Graduated,
    #[serde(rename = "volume")]
    Volume,

}

impl ToString for StripePriceTiersMode {
    fn to_string(&self) -> String {
        match self {
            Self::Graduated => String::from("graduated"),
            Self::Volume => String::from("volume"),
        }
    }
}

impl Default for StripePriceTiersMode {
    fn default() -> StripePriceTiersMode {
        Self::Graduated
    }
}




