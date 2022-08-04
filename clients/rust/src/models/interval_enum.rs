/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.99.7
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum IntervalEnum {
    #[serde(rename = "day")]
    Day,
    #[serde(rename = "month")]
    Month,
    #[serde(rename = "week")]
    Week,
    #[serde(rename = "year")]
    Year,

}

impl ToString for IntervalEnum {
    fn to_string(&self) -> String {
        match self {
            Self::Day => String::from("day"),
            Self::Month => String::from("month"),
            Self::Week => String::from("week"),
            Self::Year => String::from("year"),
        }
    }
}

impl Default for IntervalEnum {
    fn default() -> IntervalEnum {
        Self::Day
    }
}




