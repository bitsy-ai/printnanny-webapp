/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.99.5
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum TaxExemptEnum {
    #[serde(rename = "exempt")]
    Exempt,
    #[serde(rename = "none")]
    None,
    #[serde(rename = "reverse")]
    Reverse,

}

impl ToString for TaxExemptEnum {
    fn to_string(&self) -> String {
        match self {
            Self::Exempt => String::from("exempt"),
            Self::None => String::from("none"),
            Self::Reverse => String::from("reverse"),
        }
    }
}

impl Default for TaxExemptEnum {
    fn default() -> TaxExemptEnum {
        Self::Exempt
    }
}




