/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.97.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum StripeSubscriptionStatusEnum {
    #[serde(rename = "active")]
    Active,
    #[serde(rename = "canceled")]
    Canceled,
    #[serde(rename = "incomplete")]
    Incomplete,
    #[serde(rename = "incomplete_expired")]
    IncompleteExpired,
    #[serde(rename = "past_due")]
    PastDue,
    #[serde(rename = "trialing")]
    Trialing,
    #[serde(rename = "unpaid")]
    Unpaid,

}

impl ToString for StripeSubscriptionStatusEnum {
    fn to_string(&self) -> String {
        match self {
            Self::Active => String::from("active"),
            Self::Canceled => String::from("canceled"),
            Self::Incomplete => String::from("incomplete"),
            Self::IncompleteExpired => String::from("incomplete_expired"),
            Self::PastDue => String::from("past_due"),
            Self::Trialing => String::from("trialing"),
            Self::Unpaid => String::from("unpaid"),
        }
    }
}

impl Default for StripeSubscriptionStatusEnum {
    fn default() -> StripeSubscriptionStatusEnum {
        Self::Active
    }
}




