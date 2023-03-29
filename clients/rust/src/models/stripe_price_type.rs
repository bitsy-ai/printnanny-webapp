/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.131.8
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */

/// StripePriceType : * `one_time` - One-time * `recurring` - Recurring

/// * `one_time` - One-time * `recurring` - Recurring
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum StripePriceType {
    #[serde(rename = "one_time")]
    OneTime,
    #[serde(rename = "recurring")]
    Recurring,

}

impl ToString for StripePriceType {
    fn to_string(&self) -> String {
        match self {
            Self::OneTime => String::from("one_time"),
            Self::Recurring => String::from("recurring"),
        }
    }
}

impl Default for StripePriceType {
    fn default() -> StripePriceType {
        Self::OneTime
    }
}




