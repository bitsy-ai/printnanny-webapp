/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.104.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum StripeSubscriptionScheduleStatusEnum {
    #[serde(rename = "active")]
    Active,
    #[serde(rename = "canceled")]
    Canceled,
    #[serde(rename = "completed")]
    Completed,
    #[serde(rename = "not_started")]
    NotStarted,
    #[serde(rename = "released")]
    Released,

}

impl ToString for StripeSubscriptionScheduleStatusEnum {
    fn to_string(&self) -> String {
        match self {
            Self::Active => String::from("active"),
            Self::Canceled => String::from("canceled"),
            Self::Completed => String::from("completed"),
            Self::NotStarted => String::from("not_started"),
            Self::Released => String::from("released"),
        }
    }
}

impl Default for StripeSubscriptionScheduleStatusEnum {
    fn default() -> StripeSubscriptionScheduleStatusEnum {
        Self::Active
    }
}




