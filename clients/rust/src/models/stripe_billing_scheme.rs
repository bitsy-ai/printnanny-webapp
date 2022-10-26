/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.109.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum StripeBillingScheme {
    #[serde(rename = "per_unit")]
    PerUnit,
    #[serde(rename = "tiered")]
    Tiered,

}

impl ToString for StripeBillingScheme {
    fn to_string(&self) -> String {
        match self {
            Self::PerUnit => String::from("per_unit"),
            Self::Tiered => String::from("tiered"),
        }
    }
}

impl Default for StripeBillingScheme {
    fn default() -> StripeBillingScheme {
        Self::PerUnit
    }
}




