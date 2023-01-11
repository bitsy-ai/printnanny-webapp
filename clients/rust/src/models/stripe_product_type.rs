/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.121.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum StripeProductType {
    #[serde(rename = "good")]
    Good,
    #[serde(rename = "service")]
    Service,

}

impl ToString for StripeProductType {
    fn to_string(&self) -> String {
        match self {
            Self::Good => String::from("good"),
            Self::Service => String::from("service"),
        }
    }
}

impl Default for StripeProductType {
    fn default() -> StripeProductType {
        Self::Good
    }
}




