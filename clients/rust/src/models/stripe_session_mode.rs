/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.131.4
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */

/// StripeSessionMode : * `payment` - Payment * `setup` - Setup * `subscription` - Subscription

/// * `payment` - Payment * `setup` - Setup * `subscription` - Subscription
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum StripeSessionMode {
    #[serde(rename = "payment")]
    Payment,
    #[serde(rename = "setup")]
    Setup,
    #[serde(rename = "subscription")]
    Subscription,

}

impl ToString for StripeSessionMode {
    fn to_string(&self) -> String {
        match self {
            Self::Payment => String::from("payment"),
            Self::Setup => String::from("setup"),
            Self::Subscription => String::from("subscription"),
        }
    }
}

impl Default for StripeSessionMode {
    fn default() -> StripeSessionMode {
        Self::Payment
    }
}




